# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webtoon',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='webtoon',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]