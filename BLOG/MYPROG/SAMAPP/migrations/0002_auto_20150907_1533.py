# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Name',
            field=models.CharField(max_length=40),
        ),
    ]
