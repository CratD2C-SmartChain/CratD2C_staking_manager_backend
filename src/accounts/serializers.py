from rest_framework import serializers

from src.shared.validators import ethereum_address_validator


class WalletConnectSerializer(serializers.Serializer):
    address = serializers.CharField(required=True, validators=[ethereum_address_validator])
    signed_msg = serializers.CharField()
    message = serializers.CharField(min_length=32)


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class AuthMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=128)
