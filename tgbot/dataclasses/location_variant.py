from django.db import models


class LocationVariant(models.TextChoices):
    main_menu = "main_menu"
    about_me = "about_me"
    reason_to_take_me = "reason_to_take_me"
