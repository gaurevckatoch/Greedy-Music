# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-21 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackLister', '0002_auto_20160621_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='release_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]