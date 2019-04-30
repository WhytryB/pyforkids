# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_description_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description_full_2',
            field=models.TextField(verbose_name='Description_Full', blank=True, help_text='Обьяснение перед Тестом 2'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_full_3',
            field=models.TextField(verbose_name='Description_Full', blank=True, help_text='Обьяснение перед Тестом 3'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description_full',
            field=models.TextField(verbose_name='Description_Full', blank=True, help_text='Обьяснение перед Тестом 1'),
        ),
    ]
