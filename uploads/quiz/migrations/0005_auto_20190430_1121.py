# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20190429_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description_formul',
            field=models.TextField(verbose_name='Description_formul', blank=True, help_text='Формула перед тестом'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_formul_1',
            field=models.TextField(verbose_name='Description_formul', blank=True, help_text='Формула перед тестом 2'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_formul_2',
            field=models.TextField(verbose_name='Description_formul', blank=True, help_text='Формула перед тестом 3'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description_formul_3',
            field=models.TextField(verbose_name='Description_formul', blank=True, help_text='Формула перед тестом 4'),
        ),
    ]
