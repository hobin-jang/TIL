# Generated by Django 3.1.3 on 2020-11-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0023_remove_profile_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]