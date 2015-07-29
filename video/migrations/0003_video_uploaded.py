# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20150708_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='uploaded',
            field=models.DateTimeField(null=True),
        ),
    ]
