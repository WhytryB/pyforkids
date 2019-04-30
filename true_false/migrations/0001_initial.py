# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF_Question',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='quiz.Question')),
                ('correct', models.BooleanField(verbose_name='Correct', default=False, help_text='Отметьте это, если вопросЭто правда. Оставьте это пустым для ложного.')),
            ],
            options={
                'verbose_name': 'True/False Question',
                'verbose_name_plural': 'True/False Questions',
                'ordering': ['category'],
            },
            bases=('quiz.question',),
        ),
    ]
