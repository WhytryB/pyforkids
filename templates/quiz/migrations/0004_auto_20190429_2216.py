# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190429_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description_dop',
            field=models.TextField(verbose_name='Description_dop', blank=True, help_text='заголовок перед Тестом'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_dop_1',
            field=models.TextField(verbose_name='Description_dop', blank=True, help_text='заголовок перед Тестом 2'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_dop_2',
            field=models.TextField(verbose_name='Description_dop', blank=True, help_text='заголовок перед Тестом 3'),
        ),
    ]
