from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number']
        # fields = ['email', 'full_name', 'phone_number']

        # extra_kwargs = {'email': {'write_only': True}}
