from mixer.backend.django import mixer
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class Client(APIClient):
    def __init__(self, is_authenticated: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if is_authenticated:
            self.auth()

    def auth(self) -> None:
        self.user = mixer.blend(User, display_name="Rodion")
        token, _ = Token.objects.get_or_create(user=self.user)
        self.credentials(HTTP_AUTHORIZATION=f"Token {token}")
