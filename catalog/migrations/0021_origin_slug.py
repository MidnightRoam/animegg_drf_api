# Generated by Django 4.2 on 2023-05-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_type_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='origin',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
