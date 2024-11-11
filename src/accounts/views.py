from random import choice
from string import ascii_letters

from web3 import Web3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from eth_account.messages import encode_defunct
from rest_framework.authtoken.models import Token

from src.accounts.models import AdvUser
from src.accounts.errors import InvalidWalletSignature
from src.accounts.serializers import (
    AuthMessageSerializer,
    AuthTokenSerializer,
    WalletConnectAddressSerializer,
    WalletConnectSerializer,
)
from src.config import config
from src.accounts.utils import build_wallet_connect_message_key
from src.utilities import network, RedisClient


class WalletConnectView(APIView):
    """View that requires user address, message and message signed with a private key"""

    @swagger_auto_schema(
        operation_description="Connect wallet",
        request_body=WalletConnectSerializer(),
        responses={
            status.HTTP_200_OK: AuthTokenSerializer(),
            status.HTTP_400_BAD_REQUEST: InvalidWalletSignature.default_detail,
        },
    )
    def post(self, request: Request):
        redis = RedisClient()
        serializer = WalletConnectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = serializer.validated_data.get("address")
        message = serializer.validated_data.get("message")
        signature = serializer.validated_data.get("signed_msg")
        message_key = build_wallet_connect_message_key(message)
        cached_address = redis.connection.get(message_key)

        if not cached_address:
            raise InvalidWalletSignature
        
        if address.lower() != cached_address.lower():
            raise InvalidWalletSignature
        
        ecnoded_message = encode_defunct(text=message)
        recovered_address = network.rpc.eth.account.recover_message(
            ecnoded_message, signature=signature
        )
        if address.lower() != recovered_address.lower():
            raise InvalidWalletSignature

        eth_user, _ = AdvUser.objects.get_or_create(
            username__iexact=address,
            defaults={"username": Web3.to_checksum_address(address)},
        )
        with transaction.atomic():
            Token.objects.filter(user=eth_user).delete()
            token = Token.objects.create(user=eth_user)

        redis.connection.delete(message_key)

        response = AuthTokenSerializer(data={"token": token.key})
        response.is_valid(raise_exception=True)
        return Response(
            data=response.data,
            status=status.HTTP_200_OK,
        )



class WalletConnectMessageView(APIView):
    """Generates message, that the user should sign via wallet extension for authorization"""

    MESSAGE_LENGTH: int = 32

    @swagger_auto_schema(
        request_body=WalletConnectAddressSerializer,
        operation_description="Create message for wallet connection",
        responses={status.HTTP_200_OK: AuthMessageSerializer()},
    )
    def post(self, request: Request) -> Response:
        redis = RedisClient()
        serializer = WalletConnectAddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        message = "".join(
            choice(ascii_letters) for _ in range(self.MESSAGE_LENGTH)
        )
        redis.connection.set(
            build_wallet_connect_message_key(message),
            serializer.validated_data.get("address"),
            config.WALLET_CONNECT_MESSAGE_EXPIRATION_SECONDS,
        )
        response = AuthMessageSerializer(data={"message": message})
        response.is_valid(raise_exception=True)
        return Response(data=response.data, status=status.HTTP_200_OK)
