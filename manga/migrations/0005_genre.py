# Generated by Django 4.2 on 2023-05-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0004_type_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(default='', editable=False)),
            ],
        ),
    ]
