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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(verbose_name='тип', choices=[('s', 'system'), ('a', 'action'), ('m', 'message'), ('j', 'join'), ('l', 'leave'), ('n', 'notification')], max_length=1)),
                ('message', models.CharField(blank=True, verbose_name='текст сообщения', null=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='время отправки')),
                ('author', models.ForeignKey(blank=True, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='автор', null=True)),
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
                ('date', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('members', models.ManyToManyField(through='chat.Membership', verbose_name='участники', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'комната',
                'verbose_name_plural': 'комнаты',
                'ordering': ['-date'],
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
