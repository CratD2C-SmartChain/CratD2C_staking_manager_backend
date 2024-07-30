from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from src.statistic.utils import i_processor


class StatisticView(APIView):

    @method_decorator(cache_page(1200))
    def get(self, request):
        interval = i_processor.get_interval()
        return Response(f"{interval}", status=status.HTTP_200_OK)
