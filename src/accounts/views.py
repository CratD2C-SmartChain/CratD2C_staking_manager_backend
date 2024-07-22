from random import choice
from string import ascii_letters

from web3 import Web3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from eth_account.messages import encode_defunct
from rest_framework.authtoken.models import Token

from src.accounts.models import AdvUser
from src.accounts.errors import InvalidWalletSignature
from src.accounts.serializers import (
    AuthMessageSerializer,
    AuthTokenSerializer,
    WalletConnectSerializer,
)
from src.utilities import network


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
        serializer = WalletConnectSerializer(data=request.data)
        serializer.is_valid()
        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        address = serializer.data.get("address")

        message_hash = encode_defunct(text=serializer.data.get("message"))
        recovered_address = network.rpc.eth.account.recover_message(
            message_hash, signature=serializer.data.get("signed_msg")
        )
        if address.lower() != recovered_address.lower():
            raise InvalidWalletSignature

        eth_user, _ = AdvUser.objects.get_or_create(
            username__iexact=address,
            defaults={"username": Web3.to_checksum_address(address)},
        )

        Token.objects.filter(user=eth_user).delete()
        token = Token.objects.create(user=eth_user)

        response_serializer = AuthTokenSerializer(data={"token": token.key})
        response_serializer.is_valid()

        return Response(
            data=response_serializer.validated_data,
            status=status.HTTP_200_OK,
        )


class GetWalletConnectMessage(APIView):
    """Generates message, that the user should sign via wallet extension for authorization"""

    @swagger_auto_schema(
        operation_description="Get message for wallet connection",
        responses={status.HTTP_200_OK: AuthMessageSerializer()},
    )
    def get(self, request: Request) -> Response:
        generated_message = "".join(
            choice(ascii_letters) for _ in range(32)
        )
        request.session["metamask_message"] = generated_message

        serializer = AuthMessageSerializer(data={"message": generated_message})
        serializer.is_valid()

        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
