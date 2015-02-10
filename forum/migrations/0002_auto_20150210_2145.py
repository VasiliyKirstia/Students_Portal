# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Тема', 'ordering': ['solved', '-date']},
        ),
        migrations.AddField(
            model_name='topic',
            name='answers_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
            preserve_default=True,
        ),
    ]
