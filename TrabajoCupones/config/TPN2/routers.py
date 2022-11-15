
from rest_framework.routers import DefaultRouter
from .views import DescuentosViewSet

router = DefaultRouter()

router.register('', DescuentosViewSet, basename='coupon')

urlpatterns = router.urls