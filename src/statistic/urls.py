from django.urls import path

from src.statistic.views import StatisticView, DelegatorsInfoView


urlpatterns = [
    path('interval', StatisticView.as_view(), name='interval'),
    path('delegators', DelegatorsInfoView.as_view(), name='delegators'),
]
