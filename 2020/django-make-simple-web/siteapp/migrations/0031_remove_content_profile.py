# Generated by Django 3.1.3 on 2020-11-27 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0030_auto_20201128_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='profile',
        ),
    ]