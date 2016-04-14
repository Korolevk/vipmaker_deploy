# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0013_auto_20160413_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='profile',
            new_name='profile_follow',
        ),
        migrations.AddField(
            model_name='follow',
            name='profile_follower',
            field=models.CharField(default='', max_length=100),
        ),
    ]
