from django.contrib import admin

from tgbot.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    ordering = ("id",)
