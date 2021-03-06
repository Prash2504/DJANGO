# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0037_auto_20150922_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 9, 57, 828000), verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 9, 57, 829000), verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 17, 9, 57, 829000), verbose_name=b'Date'),
            preserve_default=True,
        ),
    ]
