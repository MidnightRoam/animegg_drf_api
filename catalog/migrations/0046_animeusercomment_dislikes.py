# Generated by Django 4.2 on 2023-05-24 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0045_commentdislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='animeusercomment',
            name='dislikes',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.commentdislike'),
        ),
    ]
