from django.contrib import admin

from tgbot.models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("id", "about_me_msg_id", "reason_to_take_me_msg_id")
    search_fields = ("id",)
