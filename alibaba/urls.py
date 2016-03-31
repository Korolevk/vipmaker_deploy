from django.conf.urls import include, url
from django.contrib import admin
from alibaba.views import home

urlpatterns = [
    url(r'^home/', 'alibaba.views.home', name='home'),
    url(r'^about/', 'alibaba.views.about', name='about'),
    url(r'^user/(?P<login>\w+)/', 'loginsys.views.user', name="user"),
    url(r'^news/', 'alibaba.views.news', name="news"),
    url(r'^add_follow/(?P<login>\w+)/', 'alibaba.views.follow_button', name="follow_button"),
    url(r'^follow_page/(?P<login>\w+)/', 'alibaba.views.follow_page', name="follow_page"),
    url(r'^my_followers_page/(?P<login>\w+)/', 'alibaba.views.my_followers_page', name="my_followers_page"),
    url(r'^posters/add_poster/(?P<login>\w+)/(?P<local_tz_from_query>[-\w]+)/', 'alibaba.views.add_poster', name='add_poster'),
    url(r'^poster/delete/(?P<poster_id>\w+)/(?P<username>\w+)/', 'alibaba.views.delete_poster', name='delete_poster'),
    url(r'^poster/add_like/(?P<poster_id>\w+)/(?P<username>\w+)/', 'alibaba.views.add_like', name='like'),
    url(r'^change_name/', 'alibaba.views.change_name', name='change_name'),
    url(r'^change_username/', 'alibaba.views.change_username', name='change_username'),
    url(r'^change_cover/', 'alibaba.views.change_cover', name='change_cover'),
    url(r'^base_settings/', 'alibaba.views.base_settings', name='base_settings'),
    url(r'^change_password/', 'alibaba.views.change_password', name='change_password'),
    url(r'^search/', 'alibaba.views.search', name='search'),
    url(r'^settings/', 'alibaba.views.settings', name='settings'),
    url(r'^$', 'loginsys.views.login', name='login')
]