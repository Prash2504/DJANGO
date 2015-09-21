# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0011_auto_20150921_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_present',
            name='Current_Month',
        ),
        migrations.RemoveField(
            model_name='news_present',
            name='Day',
        ),
        migrations.RemoveField(
            model_name='news_present',
            name='Year',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='Current_Month',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='Day',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='Year',
        ),
        migrations.AddField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 17, 39, 0, 490000), verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 17, 39, 0, 491000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 17, 39, 0, 490000), verbose_name=b'Date'),
        ),
    ]
