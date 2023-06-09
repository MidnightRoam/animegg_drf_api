# Generated by Django 4.2 on 2023-05-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_agerestrictions_agerestriction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agerestriction',
            old_name='value',
            new_name='age',
        ),
        migrations.AddField(
            model_name='agerestriction',
            name='abbreviation',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='agerestriction',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='agerestriction',
            name='title',
            field=models.CharField(default='', max_length=24),
        ),
    ]
