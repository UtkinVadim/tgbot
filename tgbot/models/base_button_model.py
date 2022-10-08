from django.db import models


class BaseButtonModel(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_text = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ("message_id",)
        abstract = True
