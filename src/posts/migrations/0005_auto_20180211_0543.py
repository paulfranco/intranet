# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-11 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=240, validators=[posts.models.validate_content]),
        ),
    ]
