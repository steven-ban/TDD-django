# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-06 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20170505_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]