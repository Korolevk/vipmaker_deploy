# -*- coding:utf-8 -*-
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from alibaba.forms import PosterForm, PhotoUpdateForm, CoverUpdateForm
from alibaba.models import WallPoster, Like, Photo, Cover, MyFollowers, Follow
from alibaba.other_functions_by_kirill import work_with_datetime as kirill
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q


def home(request):
    return HttpResponse('<h1>Home, sweet home<br></h1><a href="/">На главную</a>')

def about(request):
    args = {}
    args.update(csrf(request))
    args['my_login'] = auth.get_user(request).username
    # args['posters'] = WallPoster.objects.filter(username='vipmaker')[0:3]
    return render(request, 'alibaba/about.html', args)


def settings(request):
    try:
        args = {}
        args.update(csrf(request))
        # Передается фото и обложка, отображающаяся в настройках
        try:
            args['img'] = Photo.objects.get(username_photo=auth.get_user(request).username)
            args['img_url'] = args['img'].profile_photo.url
        except ObjectDoesNotExist:
            args['img_url'] = '/static/alibaba/images/addPhoto.png'
        try:
            args['cover'] = Cover.objects.get(username_cover=auth.get_user(request).username)
            args['cover_url'] = args['cover'].profile_cover.url
        except ObjectDoesNotExist:
            args['cover_url'] = '/static/alibaba/images/fon.jpg'

        args['my_login'] = auth.get_user(request).username
        args['user'] = User.objects.get(username=auth.get_user(request).username)
        args['file_error'] = None
        args['photo_update_form'] = PhotoUpdateForm(request.POST, request.FILES)
        args['cover_update_form'] = CoverUpdateForm(request.POST, request.FILES)

        if request.POST:
            args['del'] = request.POST.get('del', '')
            if args['del']:
                args['img'] = Photo.objects.get(username_photo=args['user'])
                if args['img'].profile_photo.url == '/static/alibaba/images/addPhoto.png':
                    # args['file_error'] = 'Это фото по умолчанию!'
                    return redirect('/settings/?photo=default_photo')

                # args['img'] = Photo.objects.get(username_photo=args['user'])
                args['img'].profile_photo.delete()
                args['img'].delete()

                forma = args['photo_update_form'].save(commit=False)
                user = User.objects.get(username=auth.get_user(request).username)
                forma.username_photo = auth.get_user(request).username
                forma.profile = user
                forma.poster_photo = '/static/alibaba/images/addPhoto.png'
                forma.first_name_photo = user.first_name
                forma.save()

                args['img'] = Photo.objects.get(username_photo=args['user'])
                poster_photoes = WallPoster.objects.filter(username=auth.get_user(request).username)
                poster_photoes.update(poster_photo=args['img'].profile_photo.url)
                # args['file_error'] = 'фото изменено!'
                return redirect('/settings/?photo=success_photo')

            if args['photo_update_form'].is_valid():
                if Photo.objects.filter(username_photo=args['user']).count() > 0:
                    args['img'] = Photo.objects.get(username_photo=args['user'])
                    if Photo.objects.get(username_photo=args['user']).profile_photo.url != '/static/alibaba/images/addPhoto.png':
                        args['img'].profile_photo.delete()
                        args['img'].delete()
                    else:
                        args['img'].delete()

                    forma = args['photo_update_form'].save(commit=False)
                    user = User.objects.get(username=auth.get_user(request).username)
                    forma.username_photo = auth.get_user(request).username
                    forma.profile = user
                    forma.first_name_photo = user.first_name
                    forma.save()

                    args['img'] = Photo.objects.get(username_photo=args['user'])
                    poster_photoes = WallPoster.objects.filter(username=auth.get_user(request).username)
                    poster_photoes.update(poster_photo=args['img'].profile_photo.url)
                    # args['file_error'] = 'фото изменено!'

                    follow = Follow.objects.filter(followers_username=args['user'])
                    follow.update(followers_photo=args['img'].profile_photo.url)

                    follow = Follow.objects.filter(follow_username=args['user'])
                    follow.update(follow_photo=args['img'].profile_photo.url)

                    return redirect('/settings/?photo=success_photo')

        if request.GET:
            photo = request.GET.get('photo','')
            cover = request.GET.get('cover', '')
            name = request.GET.get('name', '')
            password = request.GET.get('password','')
            login = request.GET.get('login','')
            base = request.GET.get('base', '')

            if photo == 'success_photo':
                args['photo_error'] = 'Фотография изменена'
            elif photo == 'default_photo':
                args['photo_error'] = 'Это фото по умолчанию!'
            elif cover == 'success_cover':
                args['cover_error'] = 'Обложка изменена'
            elif cover == 'error_default_cover':
                args['cover_error'] = 'Это обложка по умолчанию!'
            elif cover == 'error_unknow_cover':
                args['cover_error'] = 'Неизвестная ошибка'

            elif name == 'empty':
                args['error'] = 'Ни одного поля не оставьте пустым!'
            elif name == 'name_changed':
                args['error'] = 'Имя изменено!'
            elif name == 'name_password_error':
                args['error'] = 'Неверный пароль'

            elif password == 'empty':
                args['error'] = 'Ни одного поля не оставьте пустым'
            elif password == 'password_changed':
                args['error'] = 'Пароль успешно изменен!'
            elif password == 'password_not_equal':
                args['error'] = 'Пароли не совпадают!'
            elif password == 'error_old_pass':
                args['error'] = 'Неправильный старый пароль!'

            elif login == 'empty':
                args['login_settings_error'] = 'Ни одного поля не оставьте пустым!'
            elif login == 'good':
                args['login_settings_error'] = 'Логин изменен!'
            elif login == 'invalid_pass':
                args['login_settings_error'] = 'Неверный пароль'
            elif login == 'login_in_db':
                args['login_settings_error'] = 'Такой логин уже у другого пользователя'

            elif base == 'empty':
                args['base_settings_error'] = 'Ни одного поля не оставьте пустым!'
            elif base == 'email_good':
                args['base_settings_error'] = 'Email изменен!'
            elif login == 'invalid_pass':
                args['base_settings_error'] = 'Неверный пароль'

            return render(request, 'alibaba/settings.html', args)

    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'alibaba/settings.html', args)


def change_cover(request):
    try:
        args = {}
        args.update(csrf(request))
        args['my_login'] = auth.get_user(request).username
        args['user'] = User.objects.get(username=auth.get_user(request).username)
        args['cover_error'] = None
        args['cover_update_form'] = CoverUpdateForm(request.POST, request.FILES)
        if request.POST:
            args['del'] = request.POST.get('del', '')
            if args['del']:
                try:
                    args['cover'] = Cover.objects.get(username_cover=args['user'])
                except ObjectDoesNotExist:
                    # args['cover_error'] = 'Unknown Error!'
                    return redirect('/settings/?cover=error_unknow_cover')
                if args['cover'].profile_cover.url == '/static/alibaba/images/fon.jpg':
                    # args['file_error'] = 'Это фото по умолчанию!'
                    return redirect('/settings/?cover=error_default_cover')

                if args['cover']:
                    if Cover.objects.get(username_cover=args['user']).profile_cover.url != '/static/alibaba/images/fon.jpg':
                        args['cover'].profile_cover.delete()
                        args['cover'].delete()
                    else:
                        args['cover'].delete()
                forma = args['cover_update_form'].save(commit=False)
                user = User.objects.get(username=auth.get_user(request).username)
                forma.username_cover = auth.get_user(request).username
                forma.profile = user
                forma.poster_cover = '/static/alibaba/images/fon.jpg'
                forma.first_name_cover = user.first_name
                forma.save()
                # args['file_error'] = 'обложка изменена!'
                return redirect('/settings/?cover=success_cover')

            if args['cover_update_form'].is_valid():
                try:
                    args['cover'] = Cover.objects.get(username_cover=args['user'])
                except ObjectDoesNotExist:
                    forma = args['cover_update_form'].save(commit=False)
                    user = User.objects.get(username=auth.get_user(request).username)
                    forma.username_cover = auth.get_user(request).username
                    forma.profile = user
                    forma.first_name_cover = user.first_name
                    forma.save()
                    # args['file_error'] = 'обложка изменена!'
                    return redirect('/settings/?cover=success_cover')

                args['cover'] = Cover.objects.get(username_cover=args['user'])
                if Cover.objects.filter(username_cover=args['user']).count() > 0:
                    if Cover.objects.get(username_cover=args['user']).profile_cover.url == '/static/alibaba/images/fon.jpg':
                        args['cover'].delete()
                    else:
                        args['cover'].profile_cover.delete()
                        args['cover'].delete()
                    forma = args['cover_update_form'].save(commit=False)
                    user = User.objects.get(username=auth.get_user(request).username)
                    forma.username_cover = auth.get_user(request).username
                    forma.profile = user
                    forma.first_name_cover = user.first_name
                    forma.save()
                    # args['file_error'] = 'обложка изменена!'
                    return redirect('/settings/?cover=success_cover')
                else:
                    forma = args['cover_update_form'].save(commit=False)
                    user = User.objects.get(username=auth.get_user(request).username)
                    forma.username_cover = auth.get_user(request).username
                    forma.profile = user
                    forma.first_name_cover = user.first_name
                    forma.save()
                    # args['file_error'] = 'обложка изменена!'
                    return redirect('/settings/?cover=success_cover')
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'alibaba/settings.html', args)


def change_name(request):
    try:
        args = {}
        args.update(csrf(request))
        args['my_login'] = auth.get_user(request).username
        args['user'] = User.objects.get(username=auth.get_user(request).username)

        # Передается фото и обложка, отображающаяся в настройках
        try:
            args['img'] = Photo.objects.get(username_photo=auth.get_user(request).username)
            args['img_url'] = args['img'].profile_photo.url
        except ObjectDoesNotExist:
            args['img_url'] = '/static/alibaba/images/addPhoto.png'
        try:
            args['cover'] = Cover.objects.get(username_cover=auth.get_user(request).username)
            args['cover_url'] = args['cover'].profile_cover.url
        except ObjectDoesNotExist:
            args['cover_url'] = '/static/alibaba/images/fon.jpg'

        if request.POST:
            args['my_login'] = auth.get_user(request).username
            args['user'] = User.objects.get(username=auth.get_user(request).username)
            args['error'] = None
            name = request.POST.get('new_name', '')
            password = request.POST.get('pass', '')

            if name == '' or password == '':
                args['login_settings_error'] = 'Ни одного поля не оставьте пустым!'
                return redirect('/settings/?name=empty')

            if args['user'].check_password(password):
                args['user'].first_name = name
                args['user'].save()
                posters = WallPoster.objects.filter(username=auth.get_user(request).username)
                posters.update(name_of_user=name)
                users_in_query = Photo.objects.filter(username_photo=auth.get_user(request).username)
                users_in_query.update(first_name_photo=name)

                users_follow = Follow.objects.filter(follow_username=auth.get_user(request).username)
                users_follow.update(follow_first_name=name)
                users_followers = Follow.objects.filter(followers_username=auth.get_user(request).username)
                users_followers.update(followers_first_name=name)

                # args['error'] = 'Имя изменено!'
                return redirect('/settings/?name=name_changed')
            else:
                # args['error'] = 'Неверный пароль'
                return redirect('/settings/?name=name_password_error')
        return render(request, 'alibaba/settings.html', args)
    except ObjectDoesNotExist:
        raise Http404


def change_password(request):
    args = {}
    args.update(csrf(request))
    # Передается фото и обложка, отображающаяся в настройках
    try:
        args['img'] = Photo.objects.get(username_photo=auth.get_user(request).username)
        args['img_url'] = args['img'].profile_photo.url
    except ObjectDoesNotExist:
        args['img_url'] = '/static/alibaba/images/addPhoto.png'
    try:
        args['cover'] = Cover.objects.get(username_cover=auth.get_user(request).username)
        args['cover_url'] = args['cover'].profile_cover.url
    except ObjectDoesNotExist:
        args['cover_url'] = '/static/alibaba/images/fon.jpg'


    if request.POST:
        args['my_login'] = auth.get_user(request).username
        args['user'] = User.objects.get(username=auth.get_user(request).username)
        args['error'] = None
        old_password = request.POST.get('old_pass', '')
        new_password = request.POST.get('new_pass', '')
        new_password_2 = request.POST.get('new_pass2', '')

        if old_password == '' or new_password == '' or new_password_2 == '':
            args['login_settings_error'] = 'Ни одного поля не оставьте пустым'
            return redirect('/settings/?password=empty')

        if args['user'].check_password(old_password):
            if new_password == new_password_2:
                args['user'].set_password(new_password)
                args['user'].save()
                args['error'] = 'Пароль успешно изменен!'
                # return redirect('/settings/?password=password_changed')
                return render(request, 'alibaba/anon_user.html', args)
            else:
                # args['error'] = 'Пароли не совпадают!'
                return redirect('/settings/?password=password_not_equal')
        else:
            # args['error'] = 'Неправильный старый пароль!'
            return redirect('/settings/?password=error_old_pass')
        # return render(request, 'alibaba/settings.html', args)
    else:
        return render(request, 'alibaba/settings.html', {'error':'error'})


def change_username(request):
    args = {}
    args.update(csrf(request))
    args['my_login'] = auth.get_user(request).username
    args['user'] = User.objects.get(username=auth.get_user(request).username)

    # Передается фото и обложка, отображающаяся в настройках
    try:
        args['img'] = Photo.objects.get(username_photo=auth.get_user(request).username)
        args['img_url'] = args['img'].profile_photo.url
    except ObjectDoesNotExist:
        args['img_url'] = '/static/alibaba/images/addPhoto.png'
    try:
        args['cover'] = Cover.objects.get(username_cover=auth.get_user(request).username)
        args['cover_url'] = args['cover'].profile_cover.url
    except ObjectDoesNotExist:
        args['cover_url'] = '/static/alibaba/images/fon.jpg'

    if request.POST:
        args['wall_poster'] = WallPoster.objects.filter(username=auth.get_user(request).username)
        args['photo'] = Photo.objects.filter(username_photo=auth.get_user(request).username)
        args['cover'] = Cover.objects.filter(username_cover=auth.get_user(request).username)
        args['like'] = Like.objects.filter(username=auth.get_user(request).username)
        args['follow'] = Follow.objects.filter(follow_username=auth.get_user(request).username)
        args['followers'] = Follow.objects.filter(followers_username=auth.get_user(request).username)
        args['login_settings_error'] = None

        username = request.POST.get('username', '')
        password = request.POST.get('pass', '')

        if username == '' or password == '':
            args['login_settings_error'] = 'Ни одного поля не оставьте пустым!'
            return redirect('/settings/?login=empty')

        if User.objects.filter(username=username).count() > 0:
            args['login_settings_error'] = 'Такой логин уже у другого пользователя'
            return redirect('/settings/?login=login_in_db')
            # return render(request, 'alibaba/settings.html', args)

        if args['user'].check_password(password):

                # args['wall_poster'].username = username
                args['wall_poster'].update(username=username)
                args['photo'].update(username_photo=username)
                args['cover'].update(username_cover=username)
                args['like'].update(username=username)
                args['follow'].update(follow_username=username)
                args['followers'].update(followers_username=username)
                # args['wall_poster'].save()

                # args['photo'].username_photo = username
                # args['photo'].save()
                #
                # args['cover'].username_cover = username
                # args['cover'].save()
                #
                # args['like'].username = username
                # args['like'].save()
                #
                # args['follow'].follow_username = username
                # args['follow'].save()

                args['user'].username = username
                args['user'].save()
                args['login_settings_error'] = 'Логин изменен!'
                args['my_login'] = username
                # return render(request, 'alibaba/settings.html', args)
                return redirect('/settings/?login=good')
        else:
                args['login_settings_error'] = 'Неверный пароль'
                # return render(request, 'alibaba/settings.html', args)
                return redirect('/settings/?login=invalid_pass')
    else:
        return render(request, 'alibaba/settings.html', {'login_settings_error':'error'})


def base_settings(request):
    args = {}
    args.update(csrf(request))
    # Передается фото и обложка, отображающаяся в настройках
    try:
        args['img'] = Photo.objects.get(username_photo=auth.get_user(request).username)
        args['img_url'] = args['img'].profile_photo.url
    except ObjectDoesNotExist:
        args['img_url'] = '/static/alibaba/images/addPhoto.png'
    try:
        args['cover'] = Cover.objects.get(username_cover=auth.get_user(request).username)
        args['cover_url'] = args['cover'].profile_cover.url
    except ObjectDoesNotExist:
        args['cover_url'] = '/static/alibaba/images/fon.jpg'


    if request.POST:
        args['my_login'] = auth.get_user(request).username
        args['user'] = User.objects.get(username=auth.get_user(request).username)
        args['base_settings_error'] = None
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')

        if email == '' or password == '':
            args['login_settings_error'] = 'Ни одного поля не оставьте пустым!'
            return redirect('/settings/?base=empty')

        if args['user'].check_password(password):
            args['user'].email = email
            args['user'].save()
            # args['base_settings_error'] = 'Email изменен!'
            return redirect('/settings/?base=email_good')
        else:
            # args['base_settings_error'] = 'Неверный пароль'
            return redirect('/settings/?base=pass_invalid')
        # return render(request, 'alibaba/settings.html', args)
    else:
        return render(request, 'alibaba/settings.html', {'base_settings_error':'error'})

def news(request):
    args = {}
    args.update(csrf(request))
    args['user'] = User.objects.get(username=auth.get_user(request).username)
    args['my_login'] = auth.get_user(request).username
    u = args['user'].id

    args['i_follow'] = Follow.objects.filter(profile=args['user']).values_list('follow_username', flat=True)

    # args['a'] = Follow.objects.filter(profile=args['user']).values_list('follow_username', flat=True)

    args['posters'] = WallPoster.objects.filter(username__in=args['i_follow'])
    args['posters_count'] = WallPoster.objects.filter(username__in=args['i_follow']).count()
    return render(request, 'alibaba/news.html', args)

# --- Search Page ---
def search(request):
    if not auth.get_user(request).username:
        return render(request, 'alibaba/anon_user.html')
    args = {}
    args.update(csrf(request))
    args['my_login'] = auth.get_user(request).username
    args['user'] = User.objects.get(username=auth.get_user(request).username)
    args['search_error'] = None

    # Список тех, кто интересен мне
    args['i_follow'] = Follow.objects.filter(followers_username=args['my_login']).values_list('follow_username', flat=True)
    args['i_follow_list'] = []
    args['i_follow_list'].extend(args['i_follow'])
    # Список тех, кому интересен я
    # args['me_follow'] = Follow.objects.filter(follow_username=args['my_login']).values_list('followers_username', flat=True)
    # args['me_follow_list'] = []
    # args['me_follow_list'].extend(args['me_follow'])

    if request.GET:
        args['select_search'] = request.GET.get('select_search','')
        if args['select_search'] == 'По людям':
            args['query_search'] = request.GET.get('query_search','').strip()
            args['photoes_of_users'] = Photo.objects.filter(Q(first_name_photo__contains=args['query_search'])).count()
            if args['photoes_of_users'] > 0:
                # args['users_in_query'] = User.objects.filter(Q(first_name__contains=args['query_search']))
                args['photoes_of_users'] = Photo.objects.filter(Q(first_name_photo__contains=args['query_search']))
            else:
                args['error'] = 'Ни одного пользователя не найдено!'
        elif args['select_search'] == 'По записям':
             args['query_search'] = request.GET.get('query_search','').strip()
             args['posters_in_query'] = WallPoster.objects.filter(Q(text__contains = args['query_search'])).count()
             if args['posters_in_query'] > 0:
                args['posters_in_query'] = WallPoster.objects.filter(Q(text__contains=args['query_search']))
             else:
                args['error'] = 'Ни одной записи не найдено!'
        else:
           args['error'] = 'Ни одного пользователя не найдено!'
    else:
        return render(request, 'alibaba/search.html', args)
    return render(request, 'alibaba/search.html', args)


# --- Кнопка подписаться/отписаться
def follow_button(request, login):
    user = User.objects.get(username=login)
    my_login = auth.get_user(request).username
    # Получаем пользователя у с данным логином
    user = User.objects.get(username=login)
    # Получаем текущего пользователя
    iam = User.objects.get(username=auth.get_user(request).username)
    # Получаем фото профиля пользователя с данным логином
    photo = Photo.objects.get(username_photo=login)
    # Получаем фото профиля пользователя текущего
    photo2 = Photo.objects.get(username_photo=auth.get_user(request).username)

    # Если follow_username уже интересен человеку followers_username, то не добовляет еще одного /
    # и удаялет текуший, чтобы отписаться
    if Follow.objects.filter(follow_username=login,followers_username=iam.username).count() > 0:
        follow_object = Follow.objects.get(follow_username=login,followers_username=iam.username)
        follow_object.delete()

        if request.GET:
            if request.GET.get('from', '') == 'my_followers':
                who_page = request.GET.get('who_page')
                return redirect('/my_followers_page/{u}/'.format(u=who_page))
            elif request.GET.get('from', '') == 'follow_page':
                who_page = request.GET.get('who_page')
                return redirect('/follow_page/{u}/'.format(u=who_page))
            elif request.GET.get('from', '') == 'search':
                query_search = request.GET.get('query_search', '')
                select_search = request.GET.get('select_search', '')
                redirect_str = '/search/?query_search={q}&select_search={s}'.format(q=query_search, s=select_search)
                return redirect(redirect_str)
            else:
                return redirect('/user/{u}/'.format(u=login))

        return redirect('/user/{u}/'.format(u=login))

    Follow.objects.create(
        followers_username=iam.username,
        followers_first_name=iam.first_name,
        followers_photo=photo2.profile_photo,
        profile=iam,
        follow_username=user.username,
        follow_first_name=user.first_name,
        follow_photo=photo.profile_photo
    )

    if request.GET:
        if request.GET.get('from', '') == 'my_followers':
            who_page = request.GET.get('who_page')
            return redirect('/my_followers_page/{u}/'.format(u=who_page))
        elif request.GET.get('from', '') == 'follow_page':
            who_page = request.GET.get('who_page')
            return redirect('/follow_page/{u}/'.format(u=who_page))
        elif request.GET.get('from', '') == 'search':
                query_search = request.GET.get('query_search', '')
                select_search = request.GET.get('select_search', '')
                redirect_str = '/search/?query_search={q}&select_search={s}'.format(q=query_search, s=select_search)
                return redirect(redirect_str)
        else:
            return redirect('/user/{u}/'.format(u=login))

    return redirect('/user/{u}/'.format(u=login))


# Страница моих подписок, которые интересны мне
def follow_page(request, login):
    args = {}
    args.update(csrf(request))
    args['my_login'] = auth.get_user(request).username
    # args['user'] = User.objects.get(username=login)
    args['user'] = User.objects.get(username=login)

    # Те, на кого подписан пользователь
    args['i_follow'] = Follow.objects.filter(profile=args['user'])

    # Список тех, кто интересен мне
    args['i_follow2'] = Follow.objects.filter(followers_username=args['my_login']).values_list('follow_username', flat=True)
    args['i_follow_list_me'] = []
    args['i_follow_list_me'].extend(args['i_follow2'])

    return render(request, 'alibaba/follow.html', args)


# Страница тех людей, которым интересен я
def my_followers_page(request, login):
    args = {}
    args.update(csrf(request))
    args['my_login'] = auth.get_user(request).username
    args['user'] = User.objects.get(username=login)
    args['login'] = login

    # Ищем всех, у кого интересный человек(follow_username) Этот пользоваетль login
    args['me_follow'] = Follow.objects.filter(follow_username=args['user'].username)

    # Список тех, кто интересен мне
    args['i_follow'] = Follow.objects.filter(followers_username=args['my_login']).values_list('follow_username', flat=True)
    args['i_follow_list'] = []
    args['i_follow_list'].extend(args['i_follow'])

    # args['followers'] = Follow.objects.filter(profile_follow=args['user'].username)

    return render(request, 'alibaba/my_followers.html', args)


# --- Добавляем запись на стену ---
def add_poster(request, login):
    if request.POST:
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            forma = form.save(commit=False)
            user1 = User.objects.get(username=login)
            # user = auth.get_user(request)
            forma.name_of_user = User.objects.get(username=auth.get_user(request).username).first_name
            forma.poster = user1
            forma.who_wall = user1.username
            forma.username = User.objects.get(username=auth.get_user(request).username)
            month = datetime.datetime.now().month
            now = datetime.datetime.now().strftime("%d {mounth} %Y {v} %H:%M").format(mounth=kirill.mounths[month], v='в')
            forma.date_of_poster_add = now
            try:
                forma.poster_photo = Photo.objects.get(username_photo=auth.get_user(request).username).profile_photo.url
            except ObjectDoesNotExist:
                forma.poster_photo = '/static/alibaba/images/addPhoto.png'
            forma.save()
            return redirect('/user/{}/'.format(login))
    return redirect('/user/{}/'.format(login))


def delete_poster(request, poster_id, username):
    try:
        user = User.objects.get(username=username)
        poster = WallPoster.objects.get(id=poster_id)
        poster.poster_file.delete()
        poster.delete()
        return redirect('/user/{}/'.format(user))
    except ObjectDoesNotExist:
        raise Http404


def add_like(request, poster_id, username):
    try:
        poster = WallPoster.objects.get(id=poster_id)
        user = User.objects.get(username=username)

        if Like.objects.filter(username = auth.get_user(request).username, poster_on_wall=poster,who_likes =user.username).count() == 1:
            poster.likes -= 1
            poster.save()
            likes = Like.objects.get(username = auth.get_user(request).username,who_likes =user.username,poster_on_wall = poster)
            likes.delete()

            # Если запись найдена в поиске возвращает на стр поиска, а не на user page
            if request.GET.get('from','') == 'search':
                query_search = request.GET.get('query_search','')
                select_search = request.GET.get('select_search','')
                redirect_str = '/search/?query_search={q}&select_search={s}'.format(q=query_search,s=select_search)
                return redirect(redirect_str)
            elif request.GET.get('from','') == 'news':
                return redirect('/news/')
            return redirect('/user/{}/'.format(user.username))

        elif Like.objects.filter(username = auth.get_user(request).username, poster_on_wall=poster,who_likes =user.username).count() > 0:
            if request.GET.get('from','') == 'search':
                query_search = request.GET.get('query_search','')
                select_search = request.GET.get('select_search','')
                redirect_str = '/search/?query_search={q}&select_search={s}'.format(q=query_search,s=select_search)
                return redirect(redirect_str)
            elif request.GET.get('from','') == 'news':
                return redirect('/news/')
            return redirect('/user/{}/'.format(user.username))
        else:
            likes = Like.objects.create(username = auth.get_user(request).username,who_likes =user.username,poster_on_wall = poster)
            likes.save()
            poster.likes += 1
            poster.save()
            if request.GET.get('from','') == 'search':
                query_search = request.GET.get('query_search','')
                select_search = request.GET.get('select_search','')
                redirect_str = '/search/?query_search={q}&select_search={s}'.format(q=query_search,s=select_search)
                return redirect(redirect_str)
            elif request.GET.get('from','') == 'news':
                return redirect('/news/')
            return redirect('/user/{}/'.format(user.username))
    except ObjectDoesNotExist:
        raise Http404
