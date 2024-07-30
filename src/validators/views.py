from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import django_filters.rest_framework
from rest_framework import filters

from src.validators.serializers import (
    ValidatorSerializer,
    ValidatorCreateSerializer,
    ValidatorSetUpSerializer,
    TransactionSerializer,
    ValidatorUpdateSerializer,
)
from src.validators.models import Validator
from src.validators.utils import staking_processor
from src.validators.paginators import ValidatorPagination


class ValidatorView(ListCreateAPIView):
    model = Validator
    pagination_class = ValidatorPagination
    serializer_class = ValidatorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=address']

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort', '')
        query = Validator.objects.all()
        if sort_by:
            query = query.order_by(sort_by)
        return self.filter_queryset(query)

    @swagger_auto_schema(
        operation_description="List of validators",
        responses={status.HTTP_200_OK: ValidatorSerializer(many=True)},
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create a new validator",
        request_body=ValidatorCreateSerializer(),
        responses={
            status.HTTP_201_CREATED: ValidatorSerializer(),
        },
    )
    def post(self, request):
        serializer = ValidatorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        instance = Validator.objects.get(address=serializer.validated_data['address'])
        serializer = ValidatorSerializer(instance=instance)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ValidatorUpdateView(UpdateAPIView):
    model = Validator
    serializer_class = ValidatorUpdateSerializer
    lookup_field = 'address'


class SetUpValidatorView(APIView):
    @swagger_auto_schema(
        operation_description="Get transaction payload",
        query_serializer=ValidatorSetUpSerializer(),
        responses={status.HTTP_200_OK: ""},
    )
    def get(self, request):
        serializer = ValidatorSetUpSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validator_address = serializer.validated_data.get("address")
        validator = Validator.objects.filter(address__iexact=validator_address).first()
        if validator is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = staking_processor.deposit_as_validator(serializer.validated_data.get("commission"), serializer.validated_data.get("amount"), validator.address)
        return Response(data=data, status=status.HTTP_200_OK)


class GetTransactionView(APIView):
    @swagger_auto_schema(
        operation_description="Get transaction hash",
        responses={status.HTTP_200_OK: ""},
        query_serializer=TransactionSerializer(),
    )
    def get(self, request):
        serializer = TransactionSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        block = staking_processor.get_block(
            serializer.validated_data.get("tx_hash"),
            serializer.validated_data.get("address"),
        )
        if block is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        validator = Validator.objects.filter(address__iexact=serializer.validated_data.get("address")).first()
        if validator is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        validator.start_block = block
        validator.save()
        return Response(status=status.HTTP_200_OK)
