# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-31 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20171030_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactericon',
            name='sort_key',
            field=models.IntegerField(default=999),
        ),
    ]
