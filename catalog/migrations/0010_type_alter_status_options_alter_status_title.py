# Generated by Django 4.2 on 2023-05-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_status_anime_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('TV Series', 'Tv Series'), ('Movie', 'Movie'), ('OVA', 'Ova'), ('Special', 'Special')], default=('TV Series', 'Tv Series'), max_length=10, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Released', 'Released'), ('Announcement', 'Announcement')], default=('Announcement', 'Announcement'), max_length=12, unique=True),
        ),
    ]
