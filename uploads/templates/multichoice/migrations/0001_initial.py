# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(verbose_name='Content', max_length=1000, help_text='Введите текст ответа, который Вы хотите отобразить')),
                ('correct', models.BooleanField(verbose_name='Correct', default=False, help_text='Это правильный ответ?')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='quiz.Question')),
                ('answer_order', models.CharField(verbose_name='Answer Order', max_length=30, blank=True, null=True, choices=[('content', 'Content'), ('random', 'Random'), ('none', 'None')], help_text='Порядок, в котором многократный выборотображаются вариантах ответапользователю')),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='Question', to='multichoice.MCQuestion'),
        ),
    ]
