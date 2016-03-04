# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0002_follow_followers_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='profile_follow',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='follow',
            name='profile_followers',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
