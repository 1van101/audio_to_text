# Generated by Django 4.2.4 on 2023-08-30 11:53

import audio_to_text.audio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_alter_audio_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(upload_to=audio_to_text.audio.models.unique_filename),
        ),
    ]
