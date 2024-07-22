from rest_framework import serializers
from web3 import Web3

from src.validators.models import Validator
from src.validators.errors import AddressError, BalanceError
from src.utilities import network


class ValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validator
        fields = '__all__'


class ValidatorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Validator
        fields = (
            'name',
            'logo',
            'address',
        )

    def validate_address(self, value):
        value = value if value.startswith("0x") else "0x" + value
        if not Web3.is_address(value):
            raise AddressError
        self.check_balance(value)
        return value

    @classmethod
    def check_balance(cls, address):
        if not network.check_address(address):
            raise BalanceError


class ValidatorSetUpSerializer(serializers.Serializer):
    address = serializers.CharField()
    commission = serializers.IntegerField()
    amount = serializers.IntegerField()
