# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0011_secretkey'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secretkey',
            options={'verbose_name': 'Секретный ключ', 'verbose_name_plural': 'Секретные ключи'},
        ),
        migrations.AlterField(
            model_name='follow',
            name='profile',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
