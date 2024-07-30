from django.urls import path

from src.statistic.views import StatisticView


urlpatterns = [
    path('interval', StatisticView.as_view(), name='interval'),
]