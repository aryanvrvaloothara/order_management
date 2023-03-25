from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.order.views import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet, basename='order_detail')

urlpatterns = [
    path('', include(router.urls)),
]