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
                ('date', models.DateTimeField(default=datetime.datetime(2015, 1, 31, 13, 21, 53, 907015))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=150)),
                ('text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 1, 31, 13, 21, 53, 904497))),
                ('solved', models.BooleanField(verbose_name='Решено', default=False)),
                ('category', models.ForeignKey(verbose_name='Категория', related_name='topics', to='forum.Category')),
                ('user', models.ForeignKey(verbose_name='Автор', related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
            options={
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
