from django.shortcuts import render
import random
from .models import  Author, Rule


def home(request):
    # return HttpResponse("Hello")
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get("uppercase"):
        char.extend([chr(i) for i in range(65, 91)])
    if request.GET.get("numbers"):
        char.extend([chr(i) for i in range(48, 58)])
    if request.GET.get("spacial"):
        char.extend([chr(i) for i in range(34, 48)]) or \
        char.extend([chr(i) for i in range(58, 65)])

    psw = ''
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})


def author(request):
    pr_author = Author.object.all()
    return render(request, 'generator/author.html', {'pr_author': pr_author})


def rule(request):
    pr_rule = Rule.object.all()
    return render(request, 'generator/rule.html', {'pr_rule': pr_rule})