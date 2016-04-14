# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0016_auto_20160414_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='profile_follower',
            new_name='whoes_profile_page',
        ),
    ]
