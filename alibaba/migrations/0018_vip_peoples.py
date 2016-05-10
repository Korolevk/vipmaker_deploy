# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0017_auto_20160414_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vip_peoples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('vip_person', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Вип человек',
                'verbose_name_plural': 'Вип персоны',
            },
        ),
    ]
