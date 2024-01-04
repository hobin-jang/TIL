# Generated by Django 3.1.3 on 2020-11-20 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('siteapp', '0002_auto_20201118_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_body', models.CharField(max_length=50)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siteapp.users')),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='siteapp.content')),
            ],
        ),
    ]
