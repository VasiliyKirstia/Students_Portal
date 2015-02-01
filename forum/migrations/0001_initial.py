# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 2, 1, 16, 51, 0, 923238))),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 2, 1, 16, 51, 0, 920827))),
                ('solved', models.BooleanField(default=False, verbose_name='Решено')),
                ('category', models.ForeignKey(related_name='topics', verbose_name='Категория', to='forum.Category')),
                ('user', models.ForeignKey(related_name='topics', verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(related_name='topics', to='forum.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
