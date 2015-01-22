# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150120_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='solved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
