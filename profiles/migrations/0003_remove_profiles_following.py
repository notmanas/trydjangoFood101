# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-06 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191006_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='following',
        ),
    ]
