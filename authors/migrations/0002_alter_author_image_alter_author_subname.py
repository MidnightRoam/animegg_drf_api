# Generated by Django 4.2 on 2023-05-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='author_images/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='subname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]