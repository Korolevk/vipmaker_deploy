# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0012_auto_20160413_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='profile',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
