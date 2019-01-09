# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-28 21:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20181128_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_list',
            new_name='movie_lists',
        ),
        migrations.RenameField(
            model_name='post',
            old_name=b'review',
            new_name='reviews',
        ),
        migrations.RenameField(
            model_name='preformer',
            old_name='movie',
            new_name='movies',
        ),
        migrations.RenameField(
            model_name='review',
            old_name=b'movie',
            new_name='movies',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='preformer',
            new_name='preformers',
        ),
    ]