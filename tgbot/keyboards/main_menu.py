from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from tgbot.dataclasses import Button

MAIN_MENU = ReplyKeyboardMarkup()

about_vadim_button = KeyboardButton(Button.about_me)
reason_to_take_me = KeyboardButton(Button.reason_to_take_me)

MAIN_MENU.add(about_vadim_button, reason_to_take_me)
