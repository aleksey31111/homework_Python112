from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from .forms import TodoForm
from .models import Firstpage

# OOP
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    projects = Firstpage.objects.all()
    return render(request, 'firstpage/index.html',
                  {'projects': projects})


def home(request):
    return render(request, 'firstpage/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'firstpage/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('secondpage/secondpage.html')
            except IntegrityError:
                return render(request, 'firstpage/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует, '
                                        'Задайте другое'})
        else:
            return render(request, 'firstpage/loginuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('secondpage')


def currenttodos(request):
    return render(request, 'firstpage/currenttodos.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'firstpage/loginuser.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'firstpage/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect("currenttodos")
        except ValueError:
            return render(request, 'todo/createtodo.html',
                          {'form': TodoForm(),
                           'error': 'Переданы неверные данные Попробовать еще раз'})


menu = [
    {'title': 'Добавить статью', 'url_name': 'blog'},
    {'title': 'Войти', 'url_name': 'blog'}
]


class BlogHome(ListView):
    model = Blog
    template_name = "firstpage/blog.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('cat')


class ShowPost(DetailView):
    model = Blog
    template_name = 'firstpage/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class BlogCategory(ListView):
    model = Blog
    template_name = "firstpage/blog.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat_slug=self.kwargs['cat_slug'],
                                   is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        context['menu'] = menu
        return context
