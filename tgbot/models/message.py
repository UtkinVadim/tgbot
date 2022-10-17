from django.db import models


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ("id",)
