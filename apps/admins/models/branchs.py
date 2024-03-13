from django.db import models


class Branches(models.Model):
    address = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.address
