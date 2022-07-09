from django.shortcuts import render
from .models import Rule
def rule(request):
    pr_rule = Rule.objects.all()
    return render(request, 'rule/rule.html', {'pr_rule': pr_rule})
