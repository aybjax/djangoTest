from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm


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


def getform(request, *a, **kw):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }

    print(request.method)

    if request.method == 'POST':
        print(request.POST)
        print(type(request.POST))

    elif request.method == 'GET':
        print(request.GET)
        print(type(request.GET))

    else:
        print('NONE')

    return render(request, 'getform.html', context)
