# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161114_2100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together=set([('user', 'colour'), ('user', 'name')]),
        ),
    ]
