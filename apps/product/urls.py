from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('product', ProductViewSet, 'product')


urlpatterns = [
    path('', include(router.urls))
]