# Generated by Django 4.2 on 2023-05-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
        ('catalog', '0016_anime_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='main_characters',
            field=models.ManyToManyField(blank=True, to='characters.character'),
        ),
    ]
