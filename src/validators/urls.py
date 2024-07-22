from django.urls import path

from src.validators.views import ValidatorView, SetUpValidatorView

urlpatterns = [
    path('', ValidatorView.as_view(), name='validator'),
    path('/calldata', SetUpValidatorView.as_view(), name='set-up-validator'),
    ]
