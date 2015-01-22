# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(related_name='answers', to='forum.Author'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(related_name='answers', to='forum.Topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(related_name='topics', to='forum.Author'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(related_name='topics', to='forum.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
