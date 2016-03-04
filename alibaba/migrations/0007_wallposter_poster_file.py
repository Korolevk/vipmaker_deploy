# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0006_remove_wallposter_who_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallposter',
            name='poster_file',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
    ]
