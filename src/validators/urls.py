from django.urls import path

from src.validators.views import ValidatorView, SetUpValidatorView, GetTransactionView

urlpatterns = [
    path('', ValidatorView.as_view(), name='validator'),
    path('calldata', SetUpValidatorView.as_view(), name='set-up-validator'),
    path('transaction', GetTransactionView.as_view(), name='get-transaction'),
    ]
