from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from src.validators.serializers import ValidatorSerializer, ValidatorCreateSerializer, ValidatorSetUpSerializer, TransactionSerializer
from src.validators.models import Validator
from src.validators.utils import staking_processor


class ValidatorView(APIView):

    @swagger_auto_schema(
        operation_description="List of validators",
        responses={status.HTTP_200_OK: ValidatorSerializer(many=True)},
    )
    def get(self, request):
        validators = Validator.objects.all()
        serializer = ValidatorSerializer(validators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


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
