from rest_framework import serializers

from src.accounts.validators import ethereum_signature_validator
from src.shared.validators import ethereum_address_validator


class WalletConnectSerializer(serializers.Serializer):
    address = serializers.CharField(required=True, validators=[ethereum_address_validator])
    signed_msg = serializers.CharField(validators=[ethereum_signature_validator])
    message = serializers.CharField(min_length=32)


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class AuthMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=128)


class WalletConnectAddressSerializer(serializers.Serializer):
    address = serializers.CharField(required=True, validators=[ethereum_address_validator])
