# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0040_auto_20150924_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 20, 21, 592000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 20, 21, 592000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 20, 21, 592000), verbose_name=b'Date'),
        ),
    ]
