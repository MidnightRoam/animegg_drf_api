# Generated by Django 4.2 on 2023-05-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_about_customuser_birthday_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/user_images'),
        ),
    ]
