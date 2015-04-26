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
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'приглашение',
                'verbose_name_plural': 'приглашения',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='текст сообщения')),
                ('timestamp', models.DateTimeField(verbose_name='время отправки', auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='автор', related_name='messages')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='название', max_length=150)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='участники', through='chat.Membership')),
            ],
            options={
                'verbose_name': 'комната',
                'verbose_name_plural': 'комнаты',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(to='chat.Room', verbose_name='комната', related_name='messages'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='room',
            field=models.ForeignKey(to='chat.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invite',
            name='room',
            field=models.ForeignKey(to='chat.Room', verbose_name='комната', related_name='invites'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invite',
            name='to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='приглашенный', related_name='invites'),
            preserve_default=True,
        ),
    ]
