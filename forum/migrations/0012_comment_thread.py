# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_comment_datetime_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]
