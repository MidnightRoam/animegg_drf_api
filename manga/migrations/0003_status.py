# Generated by Django 4.2 on 2023-05-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_manga_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Released', 'Released'), ('Announcement', 'Announcement')], default=('Announcement', 'Announcement'), max_length=12, unique=True)),
                ('slug', models.SlugField(default='', editable=False)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
    ]
