# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0026_auto_20171211_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals_account',
            name='account_goals',
            field=models.TextField(verbose_name='Goal:'),
        ),
    ]
