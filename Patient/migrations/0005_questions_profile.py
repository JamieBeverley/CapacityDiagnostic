# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20170305_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Patient.Profile'),
        ),
    ]
