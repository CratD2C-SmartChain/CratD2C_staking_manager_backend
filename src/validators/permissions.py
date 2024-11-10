import hashlib
import hmac
import json

from django.utils.encoding import force_bytes
from rest_framework.permissions import BasePermission

from src.config import config


class HmacPermission(BasePermission):
    """
    Permission class that validates an API token using HMAC signatures.
    """

    def has_permission(self, request, view):
        """
        Check if the request contains a valid API token by comparing HMAC signatures.

        Args:
            request: The HTTP request object.
            view: The view for which permission is being checked.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        expected_signature = hmac.new(
            force_bytes(config.API_KEY),
            force_bytes(json.dumps(request.data, separators=(",", ":"))),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected_signature, request.META.get('HTTP_X_SIGNATURE', ''))

