from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ['email']


class VerificationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    verification_code = serializers.CharField(max_length=6)

    class Meta:
        fields = ['email', 'verification_code']
