# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='фамилия', max_length=30)),
                ('short_description', models.TextField(verbose_name='краткое описание', max_length=80)),
                ('description', ckeditor.fields.RichTextField(verbose_name='полное описание')),
            ],
            options={
                'verbose_name': 'Разработчик',
                'ordering': ['first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='заголовок', max_length=150)),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(verbose_name='описание')),
                ('text', ckeditor.fields.RichTextField(verbose_name='новость')),
            ],
            options={
                'verbose_name': 'Новость',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(verbose_name='правила')),
            ],
            options={
                'verbose_name': 'Правила',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='предложение')),
                ('user', models.ForeignKey(verbose_name='автор', related_name='suggestions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пожелание (предложение)',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
    ]