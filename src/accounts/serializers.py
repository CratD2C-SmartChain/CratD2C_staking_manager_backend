from web3 import Web3
from rest_framework import serializers
from rest_framework.validators import ValidationError


class WalletConnectSerializer(serializers.Serializer):
    address = serializers.CharField(required=True)
    signed_msg = serializers.CharField()
    message = serializers.CharField(min_length=32)

    @classmethod
    def validate_address(cls, value: str) -> str:
        value = value if value.startswith("0x") else "0x" + value
        if not Web3.is_address(value):
            raise ValidationError("Address validation error")
        return value


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class AuthMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=128)
