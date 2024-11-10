from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from src.statistic.utils import i_processor
from src.statistic.models import DelegatorsInfo


class StatisticView(APIView):

    @method_decorator(cache_page(1200))
    def get(self, request):
        try:
            interval = i_processor.get_interval()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)

        return Response(f"{interval}", status=status.HTTP_200_OK)


class DelegatorsInfoView(APIView):

    @method_decorator(cache_page(60))
    def get(self, request):
        delegators_info, _ = DelegatorsInfo.objects.get_or_create()
        return Response(f"{delegators_info.total_delegators}", status=status.HTTP_200_OK)
