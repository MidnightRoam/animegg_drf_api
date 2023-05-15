# Generated by Django 4.2 on 2023-05-15 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0025_alter_anime_main_characters'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeBookmarkList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('watched', 'Watched'), ('watching', 'Watching'), ('planned', 'planned'), ('dropped', 'Dropped'), ('postponed', 'Postponed'), ('rewatching', 'Re-watching')], default=('watching', 'Watching'), max_length=50)),
                ('anime', models.ManyToManyField(to='catalog.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
