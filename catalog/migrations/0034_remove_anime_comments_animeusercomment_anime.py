# Generated by Django 4.2 on 2023-05-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_remove_animeusercomment_anime_anime_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='comments',
        ),
        migrations.AddField(
            model_name='animeusercomment',
            name='anime',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.anime'),
        ),
    ]