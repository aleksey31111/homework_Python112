from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста',
        'date_posted': '12 мая 2022',
    },
    {
        'author': 'пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста',
        'date_posted': '13 мая 2022'
    }

]


def home(request):
    # return HttpResponse('<h1>Главная</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Мой Блог</h1>')
    return render(request, 'blog/about.html', {'title': 'О Сайте "Олины" Поделки'})