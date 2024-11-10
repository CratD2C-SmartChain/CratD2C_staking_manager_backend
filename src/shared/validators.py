from rest_framework.serializers import ValidationError
from web3 import Web3


def ethereum_address_validator(value: str) -> None:
    """
    Validates if the given value is a valid Ethereum address.
    Raises ValidationError if the address is invalid.
    """
    if not Web3.is_address(value):
        raise ValidationError("Invalid address")

