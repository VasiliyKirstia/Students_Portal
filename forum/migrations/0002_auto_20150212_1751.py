# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'ordering': ['solved', '-date']},
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
