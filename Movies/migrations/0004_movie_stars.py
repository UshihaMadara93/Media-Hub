# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_auto_20160716_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Stars',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
