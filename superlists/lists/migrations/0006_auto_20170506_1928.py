# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-06 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_item_create_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
