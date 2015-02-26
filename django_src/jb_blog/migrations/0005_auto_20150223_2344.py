# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jb_blog', '0004_auto_20150223_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 23, 44, 32, 138262, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
