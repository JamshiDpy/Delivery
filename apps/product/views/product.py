from rest_framework import viewsets

from apps.product.models import Product
from apps.product.serializers import ProductSerializer

from apps.admins.views.service import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


