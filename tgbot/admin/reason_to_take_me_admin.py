from django.contrib import admin

from tgbot.models import ReasonToTakeMe


@admin.register(ReasonToTakeMe)
class ReasonToTakeMeAdmin(admin.ModelAdmin):
    list_display = ("message_id", "message_text")
    ordering = ("message_id",)
