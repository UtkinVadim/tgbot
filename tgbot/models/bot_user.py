from django.db import models

from tgbot.dataclasses import LocationVariant, Button


class BotUser(models.Model):
    id = models.IntegerField(primary_key=True)
    about_me_msg_id = models.IntegerField(default=0)
    reason_to_take_me_msg_id = models.IntegerField(default=0)
    current_location = models.CharField(max_length=255, default=LocationVariant.main_menu)

    def refresh_location(self, message_text: str) -> None:
        if message_text == Button.next_page:
            return

        button_locations = {
            str(Button.about_me): LocationVariant.about_me,
            str(Button.reason_to_take_me): LocationVariant.reason_to_take_me,
        }
        location = button_locations.get(message_text, LocationVariant.main_menu)
        self.current_location = location
        self.save()
