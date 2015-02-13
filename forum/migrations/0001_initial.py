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
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', ckeditor.fields.RichTextField()),
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
                ('name', models.CharField(verbose_name='Название', max_length=50)),
            ],
            options={
                'verbose_name': 'Категория',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=150)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('date', models.DateTimeField()),
                ('solved', models.BooleanField(default=False, verbose_name='Решено')),
                ('answers_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(related_name='questions', to='forum.Category', verbose_name='Категория')),
                ('user', models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Тема',
                'ordering': ['solved', '-date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='questions', to='forum.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
