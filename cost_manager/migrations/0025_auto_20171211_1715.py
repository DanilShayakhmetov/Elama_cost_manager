# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0024_goals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goals',
            new_name='Goals_Account',
        ),
    ]