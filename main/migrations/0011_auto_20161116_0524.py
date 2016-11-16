# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-16 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20161116_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='colour',
            field=models.CharField(choices=[('0', 'Red'), ('1', 'Yellow'), ('2', 'Green'), ('3', 'Blue')], default='Red', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='colour',
            field=models.CharField(choices=[('0', 'Red'), ('1', 'Yellow'), ('2', 'Green'), ('3', 'Blue')], max_length=6),
        ),
    ]