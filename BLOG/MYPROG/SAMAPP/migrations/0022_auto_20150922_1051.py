# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0021_auto_20150922_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 10, 51, 50, 971000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Updated',
            field=models.CharField(default=b'Updt On:', max_length=6),
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 10, 51, 50, 971000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Updated',
            field=models.CharField(default=b'Updt On:', max_length=6),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 10, 51, 50, 971000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Updated',
            field=models.CharField(default=b'Updt On:', max_length=6),
        ),
    ]
