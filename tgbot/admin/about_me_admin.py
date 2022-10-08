from django.contrib import admin

from tgbot.models import AboutMe


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("message_id", "message_text")
    ordering = ("message_id",)
