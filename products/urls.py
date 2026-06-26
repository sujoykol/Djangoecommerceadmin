from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    FeaturedProductViewSet,
    RecentProductsView,
)

router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="products"
)

router.register(
    "featured-products",
    FeaturedProductViewSet,
    basename="featured-products"
)

urlpatterns = [
    path(
        "recent-products/",
        RecentProductsView.as_view(),
        name="recent-products"
    ),
]

urlpatterns += router.urls