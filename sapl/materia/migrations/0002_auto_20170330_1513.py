# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-30 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoacessorio',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
