from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.ProfileView, 'profile')

urlpatterns = [
    path('', include(router.urls)),
]