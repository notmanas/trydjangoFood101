# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-10 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurants_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='RestaurantLocation',
        ),
    ]
