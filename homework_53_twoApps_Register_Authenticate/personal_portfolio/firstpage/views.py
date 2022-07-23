from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from .forms import TodoForm
from .models import Firstpage


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
                           'error': 'Переданы неверные данныеюПопр еще раз'})