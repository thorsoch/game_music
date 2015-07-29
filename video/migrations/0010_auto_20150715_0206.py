# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_comment_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
