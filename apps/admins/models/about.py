from django.db import models


class About(models.Model):
    about_uz = models.TextField()
    about_ru = models.TextField()
    about_en = models.TextField()

    def __str__(self):
        return "About"
