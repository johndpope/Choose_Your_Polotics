# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20170511_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.TextField(),
        ),
    ]
