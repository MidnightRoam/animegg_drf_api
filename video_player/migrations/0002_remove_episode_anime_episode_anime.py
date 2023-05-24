# Generated by Django 4.2 on 2023-05-18 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0040_anime_related_anime'),
        ('video_player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='anime',
        ),
        migrations.AddField(
            model_name='episode',
            name='anime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='catalog.anime'),
        ),
    ]