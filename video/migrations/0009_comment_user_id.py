# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_auto_20150710_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
