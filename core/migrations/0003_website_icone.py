# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-04 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_website_favicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='icone',
            field=models.ImageField(blank=True, null=True, upload_to='icone'),
        ),
    ]
