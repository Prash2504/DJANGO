# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_KITES', '0003_auto_20150701_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_publications',
            name='Current_Month',
            field=models.CharField(max_length=20, verbose_name=b'Month', choices=[(b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'May', b'May'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')]),
            preserve_default=True,
        ),
    ]
