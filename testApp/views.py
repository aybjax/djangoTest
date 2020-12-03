from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import TestForm, TestRawForm

# Create your views here.
from .models import TestModel


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
    init = {
        'name': 'your name',
        'email': 'your email',
        'nbr': 'your nbr',
    }

    form = TestForm(request.POST or None, initial=init)
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


def rawform(request, *a, **kw):
    form = TestRawForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form)
    else:
        print(form)
    return render(request, 'getform.html', context)


def gettest(request, pk):
    # obj = get_object_or_404(TestModel, pk=pk)
    try:
        obj = TestModel.objects.get(pk=pk)
    except TestModel.DoesNotExist:
        raise Http404
    context = dict(obj=obj)
    return render(request, 'gettest.html', context)


def gettest2(request, name):
    # obj = get_object_or_404(TestModel, name=name)
    #testing commit and push
    try:
        obj = TestModel.objects.get(name=name)
    except TestModel.DoesNotExist:
        raise Http404
    context = dict(obj=obj)
    return render(request, 'gettest.html', context)
