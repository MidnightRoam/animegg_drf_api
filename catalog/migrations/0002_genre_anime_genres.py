# Generated by Django 4.2 on 2023-05-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(blank=True, to='catalog.genre'),
        ),
    ]
