# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-20 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mukluk', '0008_auto_20181001_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designedproduct',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designed_products', to='mukluk.Design'),
        ),
    ]
