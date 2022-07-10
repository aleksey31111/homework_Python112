from django.shortcuts import render
from .models import Person

def index(request):
    projects = Person.objects.all()
    return render(request, 'person/index.html',
                  {'projects': projects})
