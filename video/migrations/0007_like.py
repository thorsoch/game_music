# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_remove_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=20)),
            ],
        ),
    ]
