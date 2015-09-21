# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAMAPP', '0008_auto_20150921_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Present',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day', models.CharField(default=1, max_length=4)),
                ('Current_Month', models.CharField(max_length=20, verbose_name=b'Month', choices=[(b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'May', b'May'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')])),
                ('Year', models.CharField(max_length=6)),
                ('Data', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day', models.CharField(default=1, max_length=4)),
                ('Current_Month', models.CharField(max_length=20, verbose_name=b'Month', choices=[(b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'May', b'May'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')])),
                ('Year', models.CharField(max_length=6)),
                ('Data', models.CharField(max_length=300)),
            ],
        ),
    ]
