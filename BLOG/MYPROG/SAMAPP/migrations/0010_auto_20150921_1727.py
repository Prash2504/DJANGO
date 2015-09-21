# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0009_news_present_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='Current_Month',
        ),
        migrations.RemoveField(
            model_name='events',
            name='Day',
        ),
        migrations.RemoveField(
            model_name='events',
            name='Year',
        ),
        migrations.AddField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 17, 27, 44, 485000), verbose_name=b'Date'),
        ),
    ]
