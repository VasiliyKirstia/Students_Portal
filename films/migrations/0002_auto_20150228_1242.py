# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import films.models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_file',
            field=models.FileField(upload_to=films.models.UPLOAD_TO, verbose_name='фильм'),
            preserve_default=True,
        ),
    ]
