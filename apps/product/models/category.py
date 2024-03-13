from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Category(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name_uz


@receiver(pre_save, sender=Category)
def category_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name_en)
