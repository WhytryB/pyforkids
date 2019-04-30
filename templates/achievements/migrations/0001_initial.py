# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=75)),
                ('key', models.CharField(unique=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=75, default='')),
                ('bonus', models.IntegerField(default=0)),
                ('callback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(related_name='userachievements', to='achievements.Achievement')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
