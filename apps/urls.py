from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.users.urls')),
    path('products/', include('apps.product.urls')),
]