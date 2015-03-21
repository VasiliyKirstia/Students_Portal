# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_last_recv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'комнаты', 'ordering': ['-last_recv'], 'verbose_name': 'комната'},
        ),
        migrations.RemoveField(
            model_name='room',
            name='date',
        ),
    ]
