# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygram', '0009_image_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='follow',
        ),
        migrations.AddField(
            model_name='image',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
