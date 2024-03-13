from rest_framework import viewsets

from .service import IsAdminOrReadOnly
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()