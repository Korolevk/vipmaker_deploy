# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0007_wallposter_poster_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallposter',
            name='poster_file',
            field=models.ImageField(upload_to='files_on_wall', blank=True, null=True),
        ),
    ]
