from django.urls import path

from src.accounts.views import GetWalletConnectMessage, WalletConnectView

urlpatterns = [
    path("wallet/get_message/", GetWalletConnectMessage.as_view()),
    path("wallet/connect/", WalletConnectView.as_view()),
]
