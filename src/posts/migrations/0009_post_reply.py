# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-27 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]
