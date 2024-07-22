from django.urls import path

from src.validators.views import ValidatorView

urlpatterns = [
    path('', ValidatorView.as_view(), name='validator'),
    ]
