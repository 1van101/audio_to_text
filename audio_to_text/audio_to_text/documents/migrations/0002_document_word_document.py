# Generated by Django 4.2.4 on 2023-09-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='word_document',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
