# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-08-13 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20200813_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
