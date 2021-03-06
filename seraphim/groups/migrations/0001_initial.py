# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-28 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0004_auto_20171028_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('crt_dttm', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to='characters.Character')),
            ],
        ),
    ]
