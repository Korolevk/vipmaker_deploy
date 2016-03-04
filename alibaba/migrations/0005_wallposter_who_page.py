# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0004_auto_20160226_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallposter',
            name='who_page',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
