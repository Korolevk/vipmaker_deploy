# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^signup/', 'loginsys.views.signup', name="signup"),
    url(r'^login/', 'loginsys.views.login', name="login"),
    url(r'^logout/', 'loginsys.views.logout', name="logout"),
]