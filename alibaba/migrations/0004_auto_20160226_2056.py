# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0003_auto_20160226_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='profile_follow',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='profile_followers',
        ),
    ]
