# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-04 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='health',
        ),
        migrations.RemoveField(
            model_name='door',
            name='identifier_type',
        ),
    ]
