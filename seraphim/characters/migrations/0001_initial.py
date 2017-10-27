# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-27 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=50, verbose_name='class')),
                ('level', models.IntegerField()),
                ('base_hp', models.IntegerField()),
                ('av_short', models.CharField(max_length=50)),
                ('av_long', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CharacterIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.CharacterIcon'),
        ),
    ]
