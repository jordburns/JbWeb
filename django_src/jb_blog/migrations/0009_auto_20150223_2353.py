# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jb_blog', '0008_auto_20150223_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 23, 53, 43, 380361, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
