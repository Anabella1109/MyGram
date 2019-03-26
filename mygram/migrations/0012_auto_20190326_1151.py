# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygram', '0011_auto_20190326_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygram.Image'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
