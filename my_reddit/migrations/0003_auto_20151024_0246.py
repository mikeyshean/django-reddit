# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_reddit', '0002_auto_20151024_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 45, 30, 223534, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 45, 47, 159988, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 45, 51, 112196, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 45, 54, 512259, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 45, 59, 768462, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 2, 46, 4, 368587, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
