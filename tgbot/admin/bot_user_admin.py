from django.contrib import admin

from tgbot.models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("id", "current_message_id")
    search_fields = ("id",)
