# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161105_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parseddata',
            name='id',
        ),
        migrations.AlterField(
            model_name='parseddata',
            name='url',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
