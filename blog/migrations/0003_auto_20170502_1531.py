# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='blog/picture/no-image.jpg', upload_to='blog/picture'),
        ),
    ]