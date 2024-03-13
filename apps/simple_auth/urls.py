from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = DefaultRouter()

urlpatterns = [
    path('send-email/', views.AuthenticationView.as_view({'post': 'send_sms'}), name='send_email'),
    path('verify-code/', views.AuthenticationView.as_view({'post': 'verify_otp'}), name='verify-code'),
    path('token-refresh', TokenRefreshView.as_view(), name='token-refresh'),
]
