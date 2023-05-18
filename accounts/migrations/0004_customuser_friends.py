# Generated by Django 4.2 on 2023-05-18 12:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]