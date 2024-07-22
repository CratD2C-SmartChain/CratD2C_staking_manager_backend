from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from src.validators.serializers import ValidatorSerializer, ValidatorCreateSerializer
from src.validators.models import Validator


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


# class SetUpValidatorView(APIView):
#     @swagger_auto_schema(
#         operation_description="Get transaction payload",
#         responses={status.HTTP_200_OK: ""},
#     )
#     def get(self, request):
#         ...
