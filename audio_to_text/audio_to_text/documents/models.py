from django.contrib.auth import get_user_model
from django.db import models
import datetime

UserModel = get_user_model()


def unique_filename(_, filename):
    name, ext = filename.split('.')
    filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}-{name}.{ext}'

    return f'documents/{filename}'


class Document(models.Model):


    title = models.CharField(max_length=255)

    document_file = models.FileField(
        upload_to=unique_filename
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

    word_document = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
