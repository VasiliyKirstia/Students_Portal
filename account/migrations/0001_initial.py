# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dr', models.DateField(verbose_name='день рождения')),
                ('room_number', models.IntegerField(verbose_name='комната')),
                ('photo', models.ImageField(width_field=150, height_field=250, upload_to='', verbose_name='фото')),
                ('is_free', models.BooleanField(verbose_name='ищу вторую половинку', default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
