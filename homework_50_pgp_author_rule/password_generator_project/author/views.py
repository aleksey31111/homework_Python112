from django.shortcuts import render
from .models import Author

def author(request):
    pr_author = Author.object.all()
    return render(request, 'author/author.html', {'pr_author': pr_author})
