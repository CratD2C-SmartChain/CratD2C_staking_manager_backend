from django.urls import path

from src.accounts.views import WalletConnectMessageView, WalletConnectView

urlpatterns = [
    path("wallet/message/", WalletConnectMessageView.as_view()),
    path("wallet/connect/", WalletConnectView.as_view()),
]
