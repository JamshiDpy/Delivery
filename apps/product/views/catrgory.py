from rest_framework import generics

from apps.product.serializers import CategorySerializer
from apps.product.models import Category


class CategoryViewSet(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


