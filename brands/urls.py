from rest_framework.routers import DefaultRouter

from .views import BrandViewSet

router = DefaultRouter()

router.register(
    "",
    BrandViewSet,
    basename="brands"
)

urlpatterns = router.urls