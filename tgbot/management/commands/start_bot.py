from django.core.management.base import BaseCommand

from tgbot.bot_core import bot


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.infinity_polling()
