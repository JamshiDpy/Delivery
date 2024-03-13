from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.simple_auth.urls')),
    path('admin', include('admins.urls')),
    path('products/', include('apps.product.urls')),
]