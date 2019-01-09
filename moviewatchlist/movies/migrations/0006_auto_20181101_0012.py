# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-01 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20181101_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_list',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_list', to='movies.MovieWatchList'),
        ),
    ]