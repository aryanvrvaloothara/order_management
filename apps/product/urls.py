from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet, basename='product_detail')

urlpatterns = [
    path('', include(router.urls)),
]