# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0014_auto_20160414_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='profile_follow',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='follow',
            name='profile_follower',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
