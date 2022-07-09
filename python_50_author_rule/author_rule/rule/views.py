from django.shortcuts import render
from .models import Rule

def rule(request):
    page_rule = Rule.objects.all()
    return render(request, 'rule/rule.html', {'page_rule': page_rule})
