from rest_framework import viewsets, status
from rest_framework.response import Response


from apps.product.serializers import CategorySerializer
from .service import IsAdminOrReadOnly
from apps.product.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
