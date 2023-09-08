import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


def unique_filename(_, filename):
    name = filename.split('.')
    filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}-{name[:-1]}.{name[-1]}'

    return f'audios/{filename}'


class Audio(models.Model):
    title = models.CharField(max_length=255)

    audio_file = models.FileField(
        upload_to=unique_filename,
        # validators=[FileExtensionValidator(allowed_extensions=['mp3', 'mp4'])]
    )

    date_of_upload = models.DateTimeField(
        auto_now=True
    )

    extracted_text = models.TextField(
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    extracted_text_task_id = models.CharField(
        null=True,
        blank=True,
        max_length=55
    )

    word_document = models.CharField(max_length=255, blank=True, null=True)


