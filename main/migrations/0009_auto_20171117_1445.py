# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171117_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]