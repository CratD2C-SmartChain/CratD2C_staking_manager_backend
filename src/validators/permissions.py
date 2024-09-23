from rest_framework.permissions import BasePermission

from src.config import config


class TokenPermission(BasePermission):

    def has_permission(self, request, view):
        return request.META.get('HTTP_AUTHORIZATION', '') == config.API_KEY
