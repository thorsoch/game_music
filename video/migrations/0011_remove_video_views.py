# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20150715_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='views',
        ),
    ]
