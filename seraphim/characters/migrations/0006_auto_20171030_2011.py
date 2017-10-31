# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-31 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20171028_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactericon',
            name='name',
            field=models.CharField(default='default_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='av_long',
            field=models.TextField(blank=True, verbose_name='AV (Long), and other notes.'),
        ),
        migrations.AlterField(
            model_name='character',
            name='av_short',
            field=models.CharField(default='AV: ', max_length=50, verbose_name='AV (Short)'),
        ),
    ]
