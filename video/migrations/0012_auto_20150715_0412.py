# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0011_remove_video_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='requesto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
