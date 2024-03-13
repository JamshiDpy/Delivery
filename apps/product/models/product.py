from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    slug = models.SlugField(unique=True)
    liter = models.FloatField(null=True, blank=True)
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)
    description_en = models.CharField(max_length=300)
    image = models.ImageField(upload_to='food')
    price = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name_uz


@receiver(pre_save, sender=Product)
def product_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name_en)
