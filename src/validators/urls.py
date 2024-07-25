from django.urls import path

from src.validators.views import ValidatorView, SetUpValidatorView, GetTransactionView, ValidatorUpdateView

urlpatterns = [
    path('', ValidatorView.as_view(), name='validator'),
    path('update/<str:address>', ValidatorUpdateView.as_view(), name='update-validator'),
    path('calldata', SetUpValidatorView.as_view(), name='set-up-validator'),
    path('transaction', GetTransactionView.as_view(), name='get-transaction'),
    ]
