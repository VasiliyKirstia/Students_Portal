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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name_plural': 'категории',
                'verbose_name': 'категория',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('text', ckeditor.fields.RichTextField(verbose_name='описание')),
                ('date', models.DateTimeField(auto_now=True)),
                ('solved', models.BooleanField(default=False, verbose_name='решено')),
                ('answers_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(related_name='questions', verbose_name='категория', to='forum.Category')),
                ('user', models.ForeignKey(related_name='questions', verbose_name='автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'вопросы',
                'verbose_name': 'вопрос',
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
