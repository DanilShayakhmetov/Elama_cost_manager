# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0015_auto_20171203_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_transaction',
            name='account_jornal_status',
            field=models.CharField(choices=[('+', 'Приход'), ('-', 'Расход')], default='Приход', max_length=10),
        ),
    ]
