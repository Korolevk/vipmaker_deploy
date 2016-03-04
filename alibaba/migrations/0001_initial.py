# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username_cover', models.CharField(max_length=100, default='')),
                ('profile_cover', models.ImageField(default='/static/alibaba/images/fon.jpg', upload_to='profile_photoes')),
                ('first_name_cover', models.CharField(max_length=100, default='')),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Обложки',
                'verbose_name': 'Обложка',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('follow_username', models.CharField(max_length=100, default='')),
                ('follow_first_name', models.CharField(max_length=100, default='')),
                ('follow_photo', models.ImageField(upload_to='')),
                ('followers_username', models.CharField(max_length=100, default='')),
                ('followers_first_name', models.CharField(max_length=100, default='')),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Интересные Страницы',
                'ordering': ['follow_username'],
                'verbose_name': 'Интересная Станица',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('who_likes', models.CharField(max_length=100, default='')),
                ('username', models.CharField(max_length=100, default='')),
            ],
            options={
                'verbose_name_plural': 'Лайки',
                'verbose_name': 'Лайк на записи',
            },
        ),
        migrations.CreateModel(
            name='MyFollowers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('follower_username', models.CharField(max_length=100, default='')),
                ('follower_first_name', models.CharField(max_length=100, default='')),
                ('follower_photo', models.ImageField(upload_to='')),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Подписчики',
                'ordering': ['follower_username'],
                'verbose_name': 'Подписчик',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username_photo', models.CharField(max_length=100, default='')),
                ('profile_photo', models.ImageField(default='/static/alibaba/images/addPhoto.png', upload_to='profile_photoes')),
                ('first_name_photo', models.CharField(max_length=100, default='')),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-username_photo'],
                'verbose_name': 'Фотография',
            },
        ),
        migrations.CreateModel(
            name='WallPoster',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, default='')),
                ('poster_photo', models.ImageField(upload_to='')),
                ('name_of_user', models.CharField(max_length=100, default='')),
                ('text', models.TextField()),
                ('date_of_poster_add', models.CharField(max_length=100, default='')),
                ('likes', models.IntegerField(default=0)),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Записи',
                'verbose_name': 'Запись на стене',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='poster_on_wall',
            field=models.ForeignKey(to='alibaba.WallPoster'),
        ),
    ]
