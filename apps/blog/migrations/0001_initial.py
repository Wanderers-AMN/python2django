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
            name='AnswerComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(null=True, verbose_name=b'Answer Comments', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(null=True, verbose_name=b'Answer', blank=True)),
                ('votes', models.IntegerField(default=0, null=True, verbose_name=b'Votes', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(null=True, verbose_name=b'Question Comments', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(verbose_name=b'Question')),
                ('votes', models.IntegerField(default=0, null=True, verbose_name=b'Votes', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='user_profile',
            field=models.ForeignKey(related_name='questions_for_user_profile', to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='questioncomments',
            name='questions',
            field=models.ForeignKey(related_name='question_comments_for_Questions_table', to='blog.Questions'),
        ),
        migrations.AddField(
            model_name='questioncomments',
            name='user_profile',
            field=models.ForeignKey(related_name='question_comments_for_user_profile', to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(related_name='answers_for_Questions_table', to='blog.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user_profile',
            field=models.ForeignKey(related_name='answers_for_user_profile', to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='answercomments',
            name='answers',
            field=models.ForeignKey(related_name='answers_comments_for_Answers_table', to='blog.Answers'),
        ),
        migrations.AddField(
            model_name='answercomments',
            name='user_profile',
            field=models.ForeignKey(related_name='answers_comments_for_user_profile', to='blog.UserProfile'),
        ),
    ]
