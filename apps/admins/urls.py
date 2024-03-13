from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet, 'admin-category')
router.register('product', ProductViewSet, 'admin-product')

urlpatterns = [
    path('', include(router.urls))
]