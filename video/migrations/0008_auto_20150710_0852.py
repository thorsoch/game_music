# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='name',
            field=models.IntegerField(),
        ),
    ]
