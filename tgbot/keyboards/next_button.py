from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from tgbot.dataclasses import Button

NEXT_BUTTON = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

next_btn = KeyboardButton(Button.next)

NEXT_BUTTON.add(next_btn)
