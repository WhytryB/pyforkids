# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description_full',
            field=models.TextField(verbose_name='Description_Full', blank=True, help_text='Обьяснение перед Тестом'),
        ),
    ]
