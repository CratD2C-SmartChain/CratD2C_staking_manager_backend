from rest_framework.exceptions import APIException
from rest_framework import status


class BalanceError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Balance too low'


class ValidatorAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Validator already exists'