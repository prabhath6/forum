# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20160325_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=None),
        ),
    ]