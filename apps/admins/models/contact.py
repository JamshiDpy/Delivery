from django.db import models


class Contact(models.Model):
    name_uz = models.CharField(max_length=150,)
    name_ru = models.CharField(max_length=150,)
    name_en = models.CharField(max_length=150,)
    cantact = models.CharField(max_length=250)
