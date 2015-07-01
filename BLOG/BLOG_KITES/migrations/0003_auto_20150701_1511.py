# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_KITES', '0002_news_publications_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_publications',
            name='Current_Month',
            field=models.CharField(max_length=20, verbose_name=b'Month'),
            preserve_default=True,
        ),
    ]
