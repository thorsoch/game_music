# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video_id',
            field=models.CharField(max_length=20),
        ),
    ]
