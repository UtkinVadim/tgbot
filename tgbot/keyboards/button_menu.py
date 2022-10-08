from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from tgbot.dataclasses import Button

BUTTON_MENU = ReplyKeyboardMarkup()

main_menu = KeyboardButton(Button.main_menu)
next_page = KeyboardButton(Button.next_page)

BUTTON_MENU.add(main_menu, next_page)
