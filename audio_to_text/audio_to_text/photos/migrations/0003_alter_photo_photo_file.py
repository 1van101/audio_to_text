# Generated by Django 4.2.4 on 2023-09-07 15:04

import audio_to_text.photos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.FileField(upload_to=audio_to_text.photos.models.unique_filename),
        ),
    ]