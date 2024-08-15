from rest_framework import serializers
from web3 import Web3
from drf_extra_fields.fields import Base64ImageField

from src.validators.models import Validator
from src.validators.errors import AddressError, BalanceError
from src.utilities import network


class ValidatorSerializer(serializers.ModelSerializer):
    checkpoints = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Validator
        fields = '__all__'


class ValidatorCreateSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(required=True)

    class Meta:
        model = Validator
        fields = (
            'name',
            'logo',
            'address',
            'commission',
            'description',
            'twitter',
            'telegram',
            'website',
        )

    def validate_address(self, value):
        value = value if value.startswith("0x") else "0x" + value
        if not Web3.is_address(value):
            raise AddressError
        self.check_balance(value)
        return value

    @classmethod
    def check_balance(cls, address):
        if not network.check_balance(address):
            raise BalanceError


class ValidatorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validator
        fields = (
            'name',
            'logo',
            'description',
            'twitter',
            'telegram',
            'website',
        )


class ValidatorPostSerializer(serializers.Serializer):
    addresses = serializers.CharField(required=True)


class ValidatorSetUpSerializer(serializers.Serializer):
    address = serializers.CharField()
    commission = serializers.IntegerField()
    amount = serializers.IntegerField()


class TransactionSerializer(serializers.Serializer):
    tx_hash = serializers.CharField()
    address = serializers.CharField()


class PenaltySerializer(serializers.Serializer):
    address = serializers.CharField()
