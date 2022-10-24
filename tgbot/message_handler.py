from typing import Optional, Union

from django.db.models.fields.files import ImageFieldFile
from telebot.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from tgbot.dataclasses.messages import MY_CONTACTS
from tgbot.keyboards import NEXT_BUTTON, REMOVE_KEYBOARD
from tgbot.models import BotUser, Message as MessageModel


class MessageHandler:
    def __init__(self, tg_message: Message, user_id: int):
        self.tg_message = tg_message
        self.user, _ = BotUser.objects.get_or_create(id=user_id)

    def process(self) -> (str, Optional[ImageFieldFile], Optional[ReplyKeyboardMarkup]):
        message_text, image = self._get_message()
        keyboard = self._get_keyboard()
        return message_text, image, keyboard

    def _get_message(self) -> (str, Optional[ImageFieldFile]):
        message_id = self.user.current_message_id
        associated_message = MessageModel.objects.filter(id=message_id)

        if not associated_message.exists():
            self.user.set_finish_flag()
            self.user.refresh_from_db()
            return MY_CONTACTS, None

        message = associated_message.first()

        self.user.current_message_id += 1
        self.user.save()

        return message.text, message.image

    def _get_keyboard(self) -> Union[ReplyKeyboardMarkup, ReplyKeyboardRemove]:
        return NEXT_BUTTON if not self.user.is_finished else REMOVE_KEYBOARD
