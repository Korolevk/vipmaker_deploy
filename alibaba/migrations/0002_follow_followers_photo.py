# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='followers_photo',
            field=models.ImageField(upload_to='', default='/static/alibaba/images/addPhoto.png'),
        ),
    ]
