# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.ForeignKey(related_name='invites', to='chat.Room', verbose_name='комната')),
                ('to', models.ForeignKey(related_name='invites', to=settings.AUTH_USER_MODEL, verbose_name='приглашенный')),
            ],
            options={
                'verbose_name_plural': 'приглашения',
                'verbose_name': 'приглашение',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'комнаты', 'verbose_name': 'комната'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='type',
        ),
        migrations.RemoveField(
            model_name='room',
            name='last_recv',
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(verbose_name='текст сообщения'),
        ),
    ]
