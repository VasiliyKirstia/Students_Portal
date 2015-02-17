# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='фамилия')),
                ('short_description', models.TextField(max_length=80, verbose_name='краткое описание')),
                ('description', ckeditor.fields.RichTextField(verbose_name='полное описание')),
            ],
            options={
                'verbose_name_plural': 'разработчики',
                'verbose_name': 'разработчик',
                'ordering': ['first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(verbose_name='описание')),
                ('text', ckeditor.fields.RichTextField(verbose_name='новость')),
            ],
            options={
                'verbose_name_plural': 'новости',
                'verbose_name': 'новость',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='правила')),
            ],
            options={
                'verbose_name_plural': 'правила',
                'verbose_name': 'правила',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='предложение')),
                ('user', models.ForeignKey(related_name='suggestions', verbose_name='автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'предложения (пожелания)',
                'verbose_name': 'пожелание (предложение)',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
    ]
