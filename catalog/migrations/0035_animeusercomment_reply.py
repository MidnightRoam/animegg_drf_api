# Generated by Django 4.2 on 2023-05-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0034_remove_anime_comments_animeusercomment_anime'),
    ]

    operations = [
        migrations.AddField(
            model_name='animeusercomment',
            name='reply',
            field=models.ManyToManyField(to='catalog.animeusercomment'),
        ),
    ]
