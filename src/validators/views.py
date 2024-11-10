from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import django_filters.rest_framework
from rest_framework import filters
from django.db.models import Q
from django.db.transaction import atomic

from src.validators.serializers import (
    ValidatorSerializer,
    ValidatorCreateSerializer,
    ValidatorSetUpSerializer,
    TransactionSerializer,
    ValidatorUpdateSerializer,
    ValidatorPostSerializer,
    PenaltySerializer,
)
from src.validators.models import Validator
from src.validators.utils import contract_processor
from src.validators.paginators import ValidatorPagination
from src.validators.permissions import TokenPermission
from src.validators.errors import ValidatorAlreadyExists


class ValidatorView(ListCreateAPIView):
    model = Validator
    pagination_class = ValidatorPagination
    serializer_class = ValidatorSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['=address', 'name']

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort', '')
        query = Validator.objects.filter(
            Q(status__in=Validator.validator_view_statuses()) |
            Q(address__iexact=self.request.user.username)
        )
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
        serializer.is_valid(raise_exception=True)
        address = serializer.validated_data['address']
        with atomic():
            validator = Validator.objects.select_for_update().filter(address__iexact=address).first()
            if validator:
                if validator.status == Validator.ValidatorStatus.ARCHIVED:
                    validator.delete()
                    validator = serializer.save()
                else:
                    raise ValidatorAlreadyExists
            else:
                validator = serializer.save()
      
        serializer = ValidatorSerializer(instance=validator)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ValidatorUpdateView(UpdateAPIView):
    model = Validator
    serializer_class = ValidatorUpdateSerializer
    lookup_field = 'address'
    queryset = Validator.objects.all()


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
        data = contract_processor.deposit_as_validator(
            serializer.validated_data.get("commission"),
            serializer.validated_data.get("amount"),
            validator.address,
        )
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
        block = contract_processor.get_block_from_tx(
            serializer.validated_data.get("tx_hash"),
            serializer.validated_data.get("address"),
        )
        if block is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        validator = Validator.objects.filter(address__iexact=serializer.validated_data.get("address")).first()
        if validator is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        validator.start_block = block
        validator.status = Validator.ValidatorStatus.HEALTHY
        if validator.performance_index == 0:
            validator.performance_index = 100
        validator.save()
        return Response(status=status.HTTP_200_OK)


class ValidatorPostView(ListAPIView):

    pagination_class = ValidatorPagination
    serializer_class = ValidatorSerializer

    @swagger_auto_schema(
        operation_description="Get validators depends on body",
        responses={status.HTTP_200_OK: ValidatorSerializer(many=True)},
        request_body=ValidatorPostSerializer(),
    )
    def post(self, request):
        serializer = ValidatorPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        addresses = serializer.validated_data.get("addresses", "").split(",")
        validators = Validator.objects.filter(address__in=addresses).all()
        result = self.paginate_queryset(validators)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(result, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)


class ValidatorPenaltyView(APIView):

    permission_classes = [TokenPermission]

    def post(self, request):
        serializer = PenaltySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = serializer.validated_data.get("address")
        validator = Validator.objects.filter(address__iexact=address).first()
        if validator:
            validator.penalty = validator.penalty + 1
            validator.save()
        return Response(status=status.HTTP_200_OK)
