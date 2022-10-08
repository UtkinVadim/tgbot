from django.db.models import TextChoices


class Button(TextChoices):
    about_me = "Обо мне"
    reason_to_take_me = "10 причин почему я вам подхожу"

    next_page = "Далее"
    main_menu = "Главное меню"
