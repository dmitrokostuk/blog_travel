# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-03 20:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_pages', '0004_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 8, 3, 20, 53, 21, 16796, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
