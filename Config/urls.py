from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions


class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Delivery",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sharofidinovjamshid@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('api/v1/', include('apps.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # END AUTH
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
