from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model

from ..serializers import ProfileSerializer

User = get_user_model()


class ProfileView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User, email=request.user.email)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)
