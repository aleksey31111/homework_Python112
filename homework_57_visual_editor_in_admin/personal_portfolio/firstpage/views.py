from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate

from .forms import TodoForm
from .models import Firstpage


# OOP
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import *
from .forms import *
from .utils import *

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
                return redirect('curenttodos')
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


### BlogHome BlogCategory ###


class BlogHome(DataMixin, ListView):

    model = Blog
    template_name = "firstpage/blog.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):

    model = Blog
    template_name = 'firstpage/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class BlogCategory(DataMixin, ListView):
    model = Blog
    template_name = "firstpage/blog.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                   is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # context['menu'] = menu
        # return context
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - '+str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'firstpage/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'firstpage/login.html'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))



class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'firstpage/addpage.html'
    success_url = reverse_lazy('blog')
    login_url = reverse_lazy('blog')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'firstpage/contact.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        subject = "Message"
        body = {
            'name': form.cleaned_data['name'],
            'emal': form.cleaned_data['email'],
            'content': form.cleaned_data['content'],
        }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, form.cleaned_data['email'], ['admin@localhost'])
        except BadHeaderError:
            return HttpResponse("Найден Не Корректный Заголовок")

        return redirect('blog')

