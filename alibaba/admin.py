from django.contrib import admin
from alibaba.models import WallPoster, Like, Photo, Cover, Follow, MyFollowers, SecretKey, Vip_peoples

# class UserAdmin(admin.ModelAdmin):
#     fields = []
#
# class WallPosterAdmin(admin.ModelAdmin):
#     fields = []

admin.site.register([WallPoster, Like, Photo, Cover, Follow, MyFollowers, SecretKey, Vip_peoples])
