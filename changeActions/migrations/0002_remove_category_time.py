# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changeActions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='time',
        ),
    ]
