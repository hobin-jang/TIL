# Generated by Django 3.1.3 on 2020-11-26 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0017_auto_20201127_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siteapp.profile'),
        ),
    ]