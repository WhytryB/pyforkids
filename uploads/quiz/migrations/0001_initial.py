# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='Category', max_length=250, unique=True, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('score', models.CharField(verbose_name='Score', max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z', 32), 'Enter only digits separated by commas.', 'invalid')])),
                ('user', models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Progress',
                'verbose_name_plural': 'User progress records',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('figure', models.ImageField(verbose_name='Figure', blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('content', models.CharField(verbose_name='Question', max_length=1000, help_text='Введите текст вопроса, который Вы хотите отобразить')),
                ('explanation', models.TextField(verbose_name='Explanation', max_length=2000, blank=True, help_text='Объяснение будет показанопосле вопроса')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, null=True, to='quiz.Category')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=60)),
                ('description', models.TextField(verbose_name='Description', blank=True, help_text='Описание вопроса')),
                ('url', models.SlugField(verbose_name='user friendly url', max_length=60, help_text='юзер френдли вид url')),
                ('random_order', models.BooleanField(verbose_name='Random Order', default=False, help_text='Показать вопросы в случайный порядок или как они установлены?')),
                ('max_questions', models.PositiveIntegerField(verbose_name='Max Questions', blank=True, null=True, help_text='Количество вопросов, на которые нужно ответить при каждой попытке.')),
                ('answers_at_end', models.BooleanField(verbose_name='Answers at end', default=False, help_text='Правильный ответ НЕ показывается после вопроса ответы отображаются в конце.')),
                ('exam_paper', models.BooleanField(verbose_name='Exam Paper', default=False, help_text='Если да, то результат каждого попытка пользователя будет Хранится. Необходимо для маркировки.')),
                ('single_attempt', models.BooleanField(verbose_name='Single Attempt', default=False, help_text='Если да, то только одна попытка пользователю будет разрешено Не пользователи не могут сдать этот экзамен.')),
                ('pass_mark', models.SmallIntegerField(verbose_name='Pass Mark', blank=True, default=0, help_text='Процент, необходимый для сдачи экзамена.', validators=[django.core.validators.MaxValueValidator(100)])),
                ('success_text', models.TextField(verbose_name='Success Text', blank=True, help_text='Отображается, если пользователь проходит.')),
                ('fail_text', models.TextField(verbose_name='Fail Text', blank=True, help_text='Отображается в случае ошибки пользователя.')),
                ('draft', models.BooleanField(verbose_name='Draft', default=False, help_text='Если да, тест не отображается в списке тестов и может быть тольковзято пользователями, которые могут редактироватьвикторины.')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, null=True, to='quiz.Category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_order', models.CharField(verbose_name='Question Order', max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z', 32), 'Enter only digits separated by commas.', 'invalid')])),
                ('question_list', models.CharField(verbose_name='Question List', max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z', 32), 'Enter only digits separated by commas.', 'invalid')])),
                ('incorrect_questions', models.CharField(verbose_name='Incorrect questions', max_length=1024, blank=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z', 32), 'Enter only digits separated by commas.', 'invalid')])),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(verbose_name='Complete', default=False)),
                ('user_answers', models.TextField(verbose_name='User Answers', blank=True, default='{}')),
                ('start', models.DateTimeField(verbose_name='Start', auto_now_add=True)),
                ('end', models.DateTimeField(verbose_name='End', blank=True, null=True)),
                ('quiz', models.ForeignKey(verbose_name='Quiz', to='quiz.Quiz')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_sittings', 'Могу увидеть законченные экзамены.'),),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_category', models.CharField(verbose_name='Sub-Category', max_length=250, blank=True, null=True)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, null=True, to='quiz.Category')),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'Sub-Categories',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(verbose_name='Quiz', blank=True, to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(verbose_name='Sub-Category', blank=True, null=True, to='quiz.SubCategory'),
        ),
    ]
