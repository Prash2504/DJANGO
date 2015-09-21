# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0003_auto_20150907_1533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News_Publications',
            new_name='Events',
        ),
    ]
