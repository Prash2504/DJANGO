# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0007_auto_20150921_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='Date',
        ),
        migrations.AddField(
            model_name='events',
            name='Day',
            field=models.CharField(default=1, max_length=4),
        ),
    ]
