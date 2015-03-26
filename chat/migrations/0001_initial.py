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
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('s', 'system'), ('a', 'action'), ('m', 'message'), ('j', 'join'), ('l', 'leave'), ('n', 'notification')], verbose_name='тип', max_length=1)),
                ('message', models.CharField(verbose_name='текст сообщения', max_length=255, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='время отправки')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='автор', null=True, blank=True, related_name='messages')),
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
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='название', max_length=150)),
                ('last_recv', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='участники', through='chat.Membership')),
            ],
            options={
                'verbose_name': 'комната',
                'verbose_name_plural': 'комнаты',
                'ordering': ['-last_recv'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(to='chat.Room', verbose_name='комната'),
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
    ]
