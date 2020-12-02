from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, *args, **kwargs):
    return HttpResponse("<h1>Hello</h1>")


def home2(request, *args, **kwargs):
    context = {
        'title': 'home2',
        'body': 'home2'
    }
    return render(request, 'home2.html', context)


def local(request, *args, **kwargs):
    return render(request, 'local.html', {})

