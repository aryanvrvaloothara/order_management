from rest_framework import viewsets

from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    Viewset for operations related to product
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
