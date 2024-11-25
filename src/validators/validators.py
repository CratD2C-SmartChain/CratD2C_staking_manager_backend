from django.core.exceptions import ValidationError
from web3 import Web3

from src.validators.constants import MAX_IMAGE_FILE_SIZE_MB, BYTES_IN_MB


def validate_image_size(file) -> None:
    """
    Validate the size of the uploaded image file. Raises a ValidationError if the file size exceeds the limit.
    Args:
        file (File): The uploaded file to validate.
    Raises:
        ValidationError: If the file size is greater than the specified limit in MB.
    """
    if file.size > MAX_IMAGE_FILE_SIZE_MB * BYTES_IN_MB:
        raise ValidationError(f"Image file too large ( > {MAX_IMAGE_FILE_SIZE_MB}MB )")
    

def ethereum_address_validator(value) -> None:
    """
    Validates if the given value is a valid Ethereum address.
    Raises ValidationError if the address is invalid.
    """
    if not Web3.is_address(value):
        raise ValidationError("Invalid address")
