# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygram', '0002_auto_20190321_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygram.Profile'),
        ),
    ]
