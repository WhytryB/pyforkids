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
            name='Galery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(blank=True, null=True, default='', upload_to='person_photo')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='Имя', max_length=100, null=True)),
                ('second_name', models.CharField(verbose_name='Фамилия', max_length=100, null=True)),
                ('birthday', models.DateField(verbose_name='Дата рождения', blank=True, null=True)),
                ('sms_mes', models.CharField(verbose_name='Сообщение', max_length=100, blank=True, null=True)),
                ('users', models.OneToOneField(null=True, related_name='personshop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.AddField(
            model_name='galery',
            name='person',
            field=models.ForeignKey(null=True, related_name='galery', to='app_registration.Person'),
        ),
    ]
