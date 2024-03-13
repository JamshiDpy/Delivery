from django.db import models
from django.conf import settings


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    address = models.CharField(max_length=400)
    latitude = models.CharField(max_length=150, null=True, blank=True)
    longitude = models.CharField(max_length=150, null=True, blank=True)
    apartment = models.IntegerField()
    entrance = models.IntegerField()
    floor = models.IntegerField()

