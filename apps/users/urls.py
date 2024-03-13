from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.ProfileView, 'profile')

urlpatterns = [
    path('send-email/', views.AuthenticationView.as_view({'post': 'send_sms'}), name='send_email'),
    path('verify-code/', views.AuthenticationView.as_view({'post': 'verify_otp'}), name='verify-code'),
    path('', include(router.urls)),
]