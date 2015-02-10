# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hallway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='полное описание'),
            preserve_default=True,
        ),
    ]
