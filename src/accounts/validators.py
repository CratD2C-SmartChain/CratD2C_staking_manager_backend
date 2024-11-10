from eth_utils.hexadecimal import is_hexstr

from src.accounts.errors import InvalidWalletSignature


def is_ethereum_signature(value: str) -> bool:
    return is_hexstr(value) and len(value) == 132


def ethereum_signature_validator(value: str) -> None:
    if not is_ethereum_signature(value):
        raise InvalidWalletSignature
