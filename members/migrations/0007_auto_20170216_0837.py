# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0006_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="individualmember",
            name="bio",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="individualmember",
            name="website",
            field=models.URLField(blank=True),
        ),
    ]
