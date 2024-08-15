from django.urls import path

from src.validators.views import (
    ValidatorView,
    SetUpValidatorView,
    GetTransactionView,
    ValidatorUpdateView,
    ValidatorPostView,
    ValidatorPenaltyView
)

urlpatterns = [
    path('', ValidatorView.as_view(), name='validator'),
    path('update/<str:address>', ValidatorUpdateView.as_view(), name='update-validator'),
    path('calldata', SetUpValidatorView.as_view(), name='set-up-validator'),
    path('transaction', GetTransactionView.as_view(), name='get-transaction'),
    path('delegator', ValidatorPostView.as_view(), name='validators-delegators'),
    path('penalty', ValidatorPenaltyView.as_view(), name='validators-penalty'),
    ]
