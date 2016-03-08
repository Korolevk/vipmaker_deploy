# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0009_auto_20160301_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallposter',
            name='who_wall',
            field=models.CharField(default='', max_length=100),
        ),
    ]
