# Generated by Django 4.2.4 on 2023-09-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='extracted_text_task_id',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
