# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hallway', '0002_auto_20150209_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='suggestion',
            options={'verbose_name': 'Пожелание (предложение)', 'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='новость'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='предложение'),
            preserve_default=True,
        ),
    ]
