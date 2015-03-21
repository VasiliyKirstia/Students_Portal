# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='last_recv',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 28, 10, 42, 6, 938224, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
