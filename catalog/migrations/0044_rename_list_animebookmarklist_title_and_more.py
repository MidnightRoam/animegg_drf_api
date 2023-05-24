# Generated by Django 4.2 on 2023-05-24 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0043_alter_animeusercomment_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animebookmarklist',
            old_name='list',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='animeusercomment',
            name='likes',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.commentlike'),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_likes', to='catalog.animeusercomment'),
        ),
    ]