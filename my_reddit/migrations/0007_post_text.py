# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_reddit', '0006_auto_20151024_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.CharField(default='Sample text', max_length=2000),
            preserve_default=False,
        ),
    ]
