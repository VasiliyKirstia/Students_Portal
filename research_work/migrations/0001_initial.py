# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyPressTime',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyReleaseTime',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.IntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pack',
            name='subject',
            field=models.ForeignKey(related_name='pack_set', to='research_work.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyreleasetime',
            name='pack',
            field=models.ForeignKey(related_name='key_release_time_set', to='research_work.Pack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keypresstime',
            name='pack',
            field=models.ForeignKey(related_name='key_press_time_set', to='research_work.Pack'),
            preserve_default=True,
        ),
    ]
