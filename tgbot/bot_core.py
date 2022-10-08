from telebot import TeleBot, types

from config.settings import TG_TOKEN
from tgbot.message_handler import MessageHandler


bot = TeleBot(TG_TOKEN, parse_mode=None)


@bot.message_handler(content_types=["text"])
def base_message_handler(message: types.Message):
    message_handler = MessageHandler(message=message, user_id=message.from_user.id)
    message_text, keyboard, image = message_handler.process()

    if image:
        bot.send_photo(message.from_user.id, image, reply_markup=keyboard, caption=message_text)
    else:
        bot.send_message(message.from_user.id, message_text, reply_markup=keyboard)
