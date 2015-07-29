# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
