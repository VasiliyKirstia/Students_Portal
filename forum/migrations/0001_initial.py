# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=10)),
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
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('author', models.ForeignKey(to='forum.Author')),
                ('category', models.ForeignKey(to='forum.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='forum.Author'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(to='forum.Topic'),
            preserve_default=True,
        ),
    ]
