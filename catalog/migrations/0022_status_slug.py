# Generated by Django 4.2 on 2023-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_origin_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
