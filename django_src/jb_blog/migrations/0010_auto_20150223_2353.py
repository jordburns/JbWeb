# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jb_blog', '0009_auto_20150223_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 23, 53, 54, 233540, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
