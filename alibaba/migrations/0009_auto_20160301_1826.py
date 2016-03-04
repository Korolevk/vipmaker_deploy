# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0008_auto_20160301_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallposter',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
