from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AdvUserManager(UserManager):
    @property
    def get_name(self) -> str:
        return self.username

    def __str__(self) -> str:
        return self.get_name


class AdvUser(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_name(self) -> str:
        return self.username

    def __str__(self) -> str:
        return self.get_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
