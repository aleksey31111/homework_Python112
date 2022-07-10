from django.shortcuts import render
from .models import Author, Rule


def author(request):
    page_author = Author.objects.all()
    return render(request, 'author/author.html',
                  {'page_author': page_author})


def rule(request):
    page_rule = Rule.objects.all()
    return render(request, 'author/rule.html',
                  {'page_rule': page_rule})