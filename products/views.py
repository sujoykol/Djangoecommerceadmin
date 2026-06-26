from rest_framework import viewsets

from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer

from .filters import ProductFilter

from core.pagination import (
    ProductPagination
)
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProductPagination(PageNumberPagination):
    page_size = 9

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "page_size": self.page_size,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })

class RecentProductsView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):

        return Product.objects.filter(
            status=True
        ).order_by("-created_at")[:5]


class FeaturedProductViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(
            featured=True,
            status=True
        )

class ProductViewSet(
    viewsets.ModelViewSet
):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    pagination_class = ProductPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_class = ProductFilter

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "price",
        "created_at"
    ]