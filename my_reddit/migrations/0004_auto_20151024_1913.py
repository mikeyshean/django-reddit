# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_reddit', '0003_auto_20151024_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='my_reddit.User')),
                ('parent', models.ForeignKey(to='my_reddit.Comment')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='sub',
            field=models.ForeignKey(related_query_name=b'post', related_name='posts', to='my_reddit.Sub'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='my_reddit.Post'),
        ),
    ]
