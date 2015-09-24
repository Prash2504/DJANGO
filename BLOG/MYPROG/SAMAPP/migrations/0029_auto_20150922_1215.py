# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0028_auto_20150922_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Per_Value_for_Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Corperate', models.CharField(default=b'40%', max_length=20)),
                ('Success_Rate', models.CharField(default=b'60%', max_length=20)),
                ('Student', models.CharField(default=b'100%', max_length=20)),
                ('Trainings', models.CharField(default=b'30%', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 15, 52, 29000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='news_present',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 15, 52, 29000), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 12, 15, 52, 29000), verbose_name=b'Date'),
        ),
    ]
