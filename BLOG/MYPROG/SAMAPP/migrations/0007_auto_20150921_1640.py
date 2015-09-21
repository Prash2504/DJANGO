# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0006_auto_20150921_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Date',
            field=models.CharField(default=1, max_length=2),
        ),
    ]
