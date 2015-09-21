# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name=b'pub_date')),
            ],
        ),
        migrations.CreateModel(
            name='News_Publications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Current_Month', models.CharField(max_length=20, verbose_name=b'Month', choices=[(b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'May', b'May'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')])),
                ('Year', models.CharField(max_length=6)),
                ('Data', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=300)),
            ],
        ),
    ]
