# Generated by Django 4.2 on 2023-05-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0006_manga_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='finished',
            field=models.DateField(blank=True, null=True),
        ),
    ]
