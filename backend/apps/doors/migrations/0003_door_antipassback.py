# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-04 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0002_auto_20170204_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='antipassback',
            field=models.BooleanField(default=False),
        ),
    ]
