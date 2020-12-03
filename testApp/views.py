from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .forms import TestForm, TestRawForm

# Create your views here.
from .models import TestModel
from .viewsDir.functional import *

import django.views.generic


class ClassCreate(django.views.generic.CreateView):
    template_name = 'getform.html'
    form_class = TestForm
    queryset = TestModel.objects.all()
    success_url = '/'


class ClassGetAll(django.views.generic.ListView):
    template_name = 'gettestall.html'
    queryset = TestModel.objects.all()
    context_object_name = 'objs'


class ClassGet(django.views.generic.DetailView):
    template_name = 'gettest.html'
    queryset = TestModel.objects.all()
    context_object_name = "obj"


class ClassGet2(django.views.generic.DetailView):
    template_name = 'gettest.html'
    queryset = TestModel.objects.all()

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(TestModel, name=name)


class ClassUpdate(django.views.generic.UpdateView):
    template_name = 'getform.html'
    queryset = TestModel.objects.all()
    form_class = TestForm
    success_url = '/'


class ClassDelete(django.views.generic.DeleteView):
    template_name = 'delete.html'
    queryset = TestModel.objects.all()
    success_url = '/'
