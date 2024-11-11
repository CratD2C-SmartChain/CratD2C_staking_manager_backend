from rest_framework import serializers
from web3 import Web3
from drf_extra_fields.fields import Base64ImageField

from src.config import config
from src.shared.constants import MAX_UINT256
from src.shared.validators import ethereum_address_validator
from src.validators.models import Validator

class ValidatorSerializer(serializers.ModelSerializer):
    checkpoints = serializers.ReadOnlyField(read_only=True)
    performance_index = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Validator
        fields = '__all__'


class ValidatorCreateSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(required=True)
    address = serializers.CharField(validators=[ethereum_address_validator])
    commission = serializers.IntegerField(
        min_value=config.BLOCKCHAIN.MIN_VALIDATOR_COMMISSION, 
        max_value=config.BLOCKCHAIN.MAX_VALIDATOR_COMMISSION,
    )

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

    @classmethod
    def validate_addresses(cls, addresses):
        for address in addresses.split(","):
            if not Web3.is_address(address):
                raise serializers.ValidationError(f"Invalid address: {address}")
            
        return addresses


class ValidatorSetUpSerializer(serializers.Serializer):
    address = serializers.CharField(validators=[ethereum_address_validator])
    commission = serializers.IntegerField(
        min_value=config.BLOCKCHAIN.MIN_VALIDATOR_COMMISSION, 
        max_value=config.BLOCKCHAIN.MAX_VALIDATOR_COMMISSION,
    )
    amount = serializers.IntegerField(
        min_value=config.BLOCKCHAIN.MIN_VALIDATOR_AMOUNT, 
        max_value=MAX_UINT256,
    )


class TransactionSerializer(serializers.Serializer):
    tx_hash = serializers.CharField()
    address = serializers.CharField(validators=[ethereum_address_validator])


class PenaltySerializer(serializers.Serializer):
    address = serializers.CharField(validators=[ethereum_address_validator])
