# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=150)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now=True)),
                ('solved', models.BooleanField(verbose_name='Решено', default=False)),
                ('answers_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(verbose_name='Категория', related_name='questions', to='forum.Category')),
                ('user', models.ForeignKey(verbose_name='Автор', related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вопрос',
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
