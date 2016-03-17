# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^signup/', 'loginsys.views.signup', name="signup"),
    url(r'^login/', 'loginsys.views.login', name="login"),
    url(r'^logout/', 'loginsys.views.logout', name="logout"),
    url(r'^forgot_pass/', 'loginsys.views.forgot_pass', name="forgot_pass"),
    url(r'^send_password_on_mail/', 'loginsys.views.send_password_on_mail', name="send_password_on_mail"),
    url(r'^success_forgot/', 'loginsys.views.success_forgot', name="success_forgot"),
]