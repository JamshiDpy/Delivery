from django.db import transaction
from django.db.models import BigAutoField

from rest_framework import serializers

from apps.product.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Category
        fields = ['name_uz', 'name_ru', 'name_en', 'parent']

        # extra_kwargs = dict(parent=dict(request=False))
