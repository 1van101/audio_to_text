# Generated by Django 4.2.4 on 2023-08-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='extracted_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]