# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0002_auto_20150907_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Name',
            field=models.CharField(max_length=20),
        ),
    ]
