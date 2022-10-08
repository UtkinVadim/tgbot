from typing import Optional, Type, TYPE_CHECKING

from telebot.types import Message, ReplyKeyboardMarkup
from django.db.models.fields.files import ImageFieldFile

from tgbot.keyboards import MAIN_MENU, BUTTON_MENU
from tgbot.models import BotUser, AboutMe, ReasonToTakeMe
from tgbot.dataclasses import MessageText, LocationVariant

if TYPE_CHECKING:
    from tgbot.models.base_button_model import BaseButtonModel


class MessageHandler:
    def __init__(self, message: Message, user_id: int):
        self.message = message
        self.user, _ = BotUser.objects.get_or_create(id=user_id)

    def process(self) -> (str, ReplyKeyboardMarkup, Optional[ImageFieldFile]):
        self.user.refresh_location(self.message.text)

        message, image = self._get_message()

        keyboard = self._get_keyboard()

        return message, keyboard, image

    def _get_keyboard(self) -> ReplyKeyboardMarkup:
        self.user.refresh_from_db()

        button_menu_locations = [LocationVariant.about_me, LocationVariant.reason_to_take_me]
        is_button = self.user.current_location in button_menu_locations

        return BUTTON_MENU if is_button else MAIN_MENU

    def _get_message(self) -> (str, None):
        self.user.refresh_from_db()

        message_handlers = {
            str(LocationVariant.about_me): self._about_me,
            str(LocationVariant.reason_to_take_me): self._reason_to_take_me,
        }
        handler = message_handlers.get(self.user.current_location)

        if not handler:
            return MessageText.main_menu, None

        response, image = handler()

        return response, image

    def _about_me(self) -> (str, Optional[ImageFieldFile]):
        model = AboutMe
        field_name = "about_me_msg_id"
        return self._base_button_logic(model, field_name)

    def _reason_to_take_me(self) -> (str, Optional[ImageFieldFile]):
        model = ReasonToTakeMe
        field_name = "reason_to_take_me_msg_id"
        return self._base_button_logic(model, field_name)

    def _base_button_logic(self,
                           model: Type["BaseButtonModel"],
                           field_name: str) -> (str, Optional[ImageFieldFile]):
        current_message_id = getattr(self.user, field_name)
        message = model.objects.filter(message_id=current_message_id).first()

        if not message:
            setattr(self.user, field_name, 0)
            self.user.current_location = LocationVariant.main_menu
            self.user.save()
            self.user.refresh_from_db()
            return MessageText.main_menu, None

        message_id = current_message_id + 1
        setattr(self.user, field_name, message_id)
        self.user.save()
        self.user.refresh_from_db()

        return message.message_text, message.image
