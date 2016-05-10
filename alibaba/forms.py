# -*- coding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from alibaba.models import WallPoster, Photo, Cover
from django.contrib.auth.models import User


class PosterForm(ModelForm):
    class Meta():
        model = WallPoster
        fields = ['text','poster_file']
        widgets = {
            'text': forms.Textarea(attrs={
                                            'wrap': 'virtual',
                                            'class': 'textarea',
                                            'name': 'article_textarea',
                                            'placeholder': 'Что у вас нового?',
                                            'cols': '53',
                                            'rows': '5',
                                         }),
            'poster_file': forms.FileInput(attrs={
                                            'type': 'file',
                                            'name': 'poster_file',
                                            'id': 'poster_file',
                                            'class': 'poster_file',
                                         })
        }


class PhotoUpdateForm(ModelForm):
    class Meta():
        model = Photo
        fields = ['profile_photo']
        widgets = {
            'profile_photo': forms.FileInput(attrs={
                                            'class': '_input',
                                            'name': 'profile_photo',
                                         })
        }

class CoverUpdateForm(ModelForm):
    class Meta():
        model = Cover
        fields = ['profile_cover']
        widgets = {
            'profile_cover': forms.FileInput(attrs={
                                            'class': '_input',
                                            'name': 'profile_cover',
                                         })
        }


# class SignupForm(ModelForm):
#     class Meta():
#         model = User
#         fields = ['username','first_name', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                                                 'class': 'email',
#                                                 'name': 'email',
#                                                 'placeholder': 'Логин'
#                                             }),
#             'first_name': forms.TextInput(attrs={
#                                                 'class': 'first_name',
#                                                 'name': 'first_name',
#                                                 'placeholder': 'Имя и фамилия'
#                                             }),
#             'password': forms.PasswordInput(attrs={
#                                                 'class': 'password',
#                                                 'name': 'password',
#                                                 'placeholder': 'Пароль'
#                                             }),