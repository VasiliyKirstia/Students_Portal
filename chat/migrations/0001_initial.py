# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(choices=[('s', 'system'), ('a', 'action'), ('m', 'message'), ('j', 'join'), ('l', 'leave'), ('n', 'notification')], max_length=1)),
                ('message', models.CharField(null=True, blank=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, blank=True, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(to='chat.Room'),
            preserve_default=True,
        ),
    ]
