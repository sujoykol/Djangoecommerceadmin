from rest_framework import viewsets

from .models import Banner
from .serializers import BannerSerializer


class BannerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Banner.objects.filter(
        is_active=True
    ).order_by("order")

    serializer_class = BannerSerializer