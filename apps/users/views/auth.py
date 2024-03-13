import random

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache
from django.contrib.auth import get_user_model
from ..serializers import EmailSerializer, VerificationEmailSerializer, ProfileSerializer
from apps.users.views.service import send_otp


User = get_user_model()


class AuthenticationView(viewsets.ViewSet):
    @swagger_auto_schema(request_body=EmailSerializer)
    def send_sms(self, request):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            verification_code = random.randint(100_000, 1_000_000)
            if send_otp(mail=email, otp=verification_code):
                cache.set(email, verification_code, 300)
                return Response({"message": "SMS sent successfully"}, status=status.HTTP_200_OK)
            raise Exception({"message": "Send OTP Failed"})

        return Response(serializer.errors)

    @swagger_auto_schema(request_body=VerificationEmailSerializer())
    def verify_otp(self, request):
        serializer = VerificationEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            cache_code = cache.get(email)
            vrf_code = serializer.validated_data['verification_code']

            if str(cache_code) == str(vrf_code):
                user, create = User.objects.get_or_create(email=email)
                if create:
                    user.save()
                token = RefreshToken.for_user(user)
                return Response({"refresh": str(token), "access": str(token.access_token)}, status.HTTP_200_OK)

            return Response({"message": "Invalid verification code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User, email=request.user.email)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)

