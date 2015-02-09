# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField()),
                ('solved', models.BooleanField(verbose_name='Решено', default=False)),
                ('category', models.ForeignKey(verbose_name='Категория', to='forum.Category', related_name='topics')),
                ('user', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL, related_name='topics')),
            ],
            options={
                'ordering': ['solved', '-date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(to='forum.Topic', related_name='topics'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='answers'),
            preserve_default=True,
        ),
    ]
