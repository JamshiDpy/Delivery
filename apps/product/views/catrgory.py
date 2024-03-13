from rest_framework import status, viewsets, mixins, permissions
from rest_framework import generics
from rest_framework.response import Response

from apps.product.serializers import CategorySerializer
from apps.product.models import Category

from .service import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data)
    #     return Response({"s": 1})
