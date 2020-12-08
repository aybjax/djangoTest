from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ExtendedUserCreationForm, CustomCreateUserForm
from testApp.forms import TestForm


# Create your views here.
def index(request, *a, **kw):
    return HttpResponse("<h1>Hello</h1>")


def registerUser(request, *a, **kw):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            messages.success(request, 'Account created successfully')
            # return redirect(reverse('userstuff:index'))
        else:
            print("sad")
    elif request.method == 'GET':
        form = UserCreationForm()
    context = {
            'form': form
    }
    return render(request, 'register.html', context)


def registerUserPlusEmail(request, *args, **kwargs):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            messages.success(request, 'Account created successfully')
            # return redirect(reverse('userstuff:index'))
        else:
            print("sad")
    elif request.method == 'GET':
        form = ExtendedUserCreationForm()
    context = {
            'form': form
    }
    print(form)
    return render(request, 'register.html', context)


def registerCustomUser(request, *a, **kw):
    if request.method == 'POST':
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            messages.success(request, 'Account created successfully')
            # return redirect(reverse('userstuff:index'))
        else:
            print("sad")
    elif request.method == 'GET':
        form = CustomCreateUserForm()
    context = {
            'form': form
    }
    return render(request, 'register.html', context)


def twoforms(request, *a, **kw):
    if request.method == 'POST':
        form1 = CustomCreateUserForm(request.POST)
        form2 = TestForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            print("success")
            messages.success(request, 'Account created successfully')
            # return redirect(reverse('userstuff:index'))
        else:
            print("sad")
    elif request.method == 'GET':
        form1 = CustomCreateUserForm()
        form2 = TestForm()
    context = {
            'form': form1,
            'form2': form2
    }
    return render(request, 'register.html', context)
