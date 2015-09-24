# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0038_auto_20150924_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 17, 15, 991000), verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 17, 15, 991000), verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 17, 15, 991000), verbose_name=b'Date'),
            preserve_default=True,
        ),
    ]
