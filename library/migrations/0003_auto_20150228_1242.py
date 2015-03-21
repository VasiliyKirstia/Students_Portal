# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20150217_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(upload_to=library.models.UPLOAD_TO, verbose_name='книга'),
            preserve_default=True,
        ),
    ]
