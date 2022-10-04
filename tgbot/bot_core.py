from telebot import TeleBot, types

from tgbot.dataclasses import Button
from config.settings import TG_TOKEN

bot = TeleBot(TG_TOKEN, parse_mode=None)

markup = types.ReplyKeyboardMarkup()

about_vadim_button = types.KeyboardButton(Button.about_vadim)
button_2 = types.KeyboardButton(Button.button_2)
button_3 = types.KeyboardButton(Button.button_3)
button_4 = types.KeyboardButton(Button.button_4)

markup.add(about_vadim_button, button_2)
markup.add(button_3, button_4)


@bot.message_handler(commands=["start"])
def start(message: types.Message) -> None:
    bot.send_message(message.from_user.id, "Главное меню:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def message_handler(message: types.Message):
    button_funcs = {
        str(Button.about_vadim.value): about_vadim_button_handler,
        str(Button.button_2.value): button_2_handler,
        str(Button.button_3.value): button_3_handler,
        str(Button.button_4.value): button_4_handler
    }

    func = button_funcs.get(message.text)
    if not func:
        bot.send_message(message.from_user.id, "Главное меню:", reply_markup=markup)
        return

    func(message)


def about_vadim_button_handler(message: types.Message):
    bot.send_message(message.from_user.id, "Это обо мне!")


def button_2_handler(message: types.Message):
    bot.send_message(message.from_user.id, "button 2")


def button_3_handler(message: types.Message):
    bot.send_message(message.from_user.id, "button 3")


def button_4_handler(message: types.Message):
    bot.send_message(message.from_user.id, "button 4")
