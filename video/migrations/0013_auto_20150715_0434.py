# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0012_auto_20150715_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesto',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requesto',
            name='user_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
