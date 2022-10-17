# Generated by Django 4.1.2 on 2022-10-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BotUser",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("current_message_id", models.IntegerField(default=0)),
                ("is_finished", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("text", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]