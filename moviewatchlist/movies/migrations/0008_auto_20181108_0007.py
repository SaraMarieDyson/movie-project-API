# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-08 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20181101_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_list',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_list',
            field=models.ManyToManyField(to='movies.MovieWatchList'),
        ),
    ]
