# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=200, upload_to='', width_field=150)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=2000)),
                ('time', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=2000)),
                ('linkText', models.CharField(max_length=250)),
                ('isCompleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changeActions.Category')),
            ],
        ),
    ]
