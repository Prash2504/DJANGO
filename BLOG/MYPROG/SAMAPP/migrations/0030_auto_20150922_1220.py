# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0029_auto_20150922_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 20, 47, 166000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 20, 47, 166000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 20, 47, 166000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='per_value_for_home',
            name='Corperate',
            field=models.CharField(default=b'40%', max_length=10),
        ),
        migrations.AlterField(
            model_name='per_value_for_home',
            name='Student',
            field=models.CharField(default=b'100%', max_length=10),
        ),
        migrations.AlterField(
            model_name='per_value_for_home',
            name='Success_Rate',
            field=models.CharField(default=b'60%', max_length=10),
        ),
        migrations.AlterField(
            model_name='per_value_for_home',
            name='Trainings',
            field=models.CharField(default=b'30%', max_length=10),
        ),
    ]
