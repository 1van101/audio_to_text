from django.contrib.auth import get_user_model
from django.db import models
import datetime

UserModel = get_user_model()


def unique_filename(_, filename):
    name, ext = filename.split('.')
    filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}-{name}.{ext}'

    return f'photos/{filename}'


class Photo(models.Model):
    CHOICES = (
        ('eng', 'English'),
        ('bul', 'Bulgarian'),
        ('deu', 'German'),
    )

    title = models.CharField(max_length=255)

    photo_file = models.ImageField(
        upload_to=unique_filename
    )

    date_of_upload = models.DateTimeField(
        auto_now=True

    )

    extracted_text = models.TextField(
        null=True,
        blank=True
    )

    language = models.CharField(
        choices=CHOICES,
        max_length=max([len(x[1]) for x in CHOICES])
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
