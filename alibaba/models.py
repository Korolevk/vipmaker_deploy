# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime, timezone
from django.contrib.auth.models import User


class SecretKey(models.Model):
    class Meta():
        verbose_name = "Секретный ключ"
        verbose_name_plural = "Секретные ключи"
    secret_key = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.secret_key


class WallPoster(models.Model):
    class Meta():
        verbose_name = "Запись на стене"
        verbose_name_plural = "Записи"

    poster = models.ForeignKey(User)
    username = models.CharField(max_length=100, default='')
    poster_photo = models.ImageField()
    poster_file = models.ImageField(null=True, blank=True, upload_to='files_on_wall')
    name_of_user = models.CharField(max_length=100, default='')
    text = models.TextField(blank=True)
    date_of_poster_add = models.CharField(max_length=100, default='')
    likes = models.IntegerField(default=0)
    who_wall = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.text+' | '+self.name_of_user


class Photo(models.Model):
    class Meta():
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-username_photo',]
    profile = models.ForeignKey(User)
    username_photo = models.CharField(max_length=100, default='')
    profile_photo = models.ImageField(upload_to='profile_photoes', default='/static/alibaba/images/addPhoto.png')
    first_name_photo = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.username_photo+"'s profile photo"


class Cover(models.Model):
    class Meta():
        verbose_name = 'Обложка'
        verbose_name_plural = 'Обложки'
    # rand = models.CharField(max_length=100, verbose_name='')
    profile = models.ForeignKey(User)
    username_cover = models.CharField(max_length=100, default='')
    profile_cover = models.ImageField(upload_to='profile_photoes', default='/static/alibaba/images/fon.jpg')
    first_name_cover = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.username_cover+"'s profile cover"


class Like(models.Model):
    class Meta():
        verbose_name = 'Лайк на записи'
        verbose_name_plural = 'Лайки'
    # Кому лайкнули запись
    who_likes = models.CharField(max_length=100, default='')
    poster_on_wall = models.ForeignKey(WallPoster)
    # Кто лайкнул запись
    username = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.who_likes


class MyFollowers(models.Model):
    class Meta():
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        ordering = ['follower_username']
    profile = models.ForeignKey(User)
    follower_username = models.CharField(max_length=100, default='')
    follower_first_name = models.CharField(max_length=100, default='')
    follower_photo = models.ImageField()

    def __str__(self):
        return self.follower_username


class Follow(models.Model):
    class Meta():
        verbose_name = 'Интересная Станица'
        verbose_name_plural = 'Интересные Страницы'
        ordering = ['follow_username']

    profile_follow = models.ForeignKey(User)
    whoes_profile_page = models.CharField(max_length=100, default='')

    follow_username = models.CharField(max_length=100, default='')
    follow_first_name = models.CharField(max_length=100, default='')
    follow_photo = models.ImageField()

    followers_username = models.CharField(max_length=100, default='')
    followers_first_name = models.CharField(max_length=100, default='')
    followers_photo = models.ImageField(default='/static/alibaba/images/addPhoto.png')

    def __str__(self):
        return 'User '+self.followers_username+' following '+self.follow_username

