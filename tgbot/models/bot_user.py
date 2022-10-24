from django.db import models


class BotUser(models.Model):
    id = models.IntegerField(primary_key=True)
    current_message_id = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)

    def set_finish_flag(self) -> None:
        if not self.is_finished:
            self.is_finished = True
            self.save()
