# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Floor",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("ip_addr", models.CharField(max_length=255)),
                ("last_query_time", models.DateTimeField(blank=True, null=True)),
            ],
        )
    ]
