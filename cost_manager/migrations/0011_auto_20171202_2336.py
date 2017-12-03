# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0010_delete_test_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='acceptor',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost_manager.Variations'),
        ),
    ]
