# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-08 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20191007_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
