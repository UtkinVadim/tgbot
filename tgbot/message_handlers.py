from telebot import types

from tgbot.bot_core import bot


@bot.message_handler(commands=["help"])
def help_handler(message: types.Message) -> None:
    bot.send_message(message.from_user.id, "Test help")
