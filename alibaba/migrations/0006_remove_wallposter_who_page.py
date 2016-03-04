# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0005_wallposter_who_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallposter',
            name='who_page',
        ),
    ]
