from django.shortcuts import render, get_object_or_404

from .models import Secondpage


def secondpage(request):
    secondpage = Secondpage.objects.order_by('-date')
    return render(request, 'secondpage/secondpage.html', {'secondpages': secondpage})

def detail(request, secondpage_id):
    secondpage = get_object_or_404(Secondpage, pk=secondpage_id)
    return render(request, 'secondpage/details.html', {'id': secondpage})