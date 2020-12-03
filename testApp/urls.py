"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "testApp"
urlpatterns = [
    path('test/', views.home, name='home'),
    path('test2/', views.home2, name='home2'),
    path('local/', views.local, name='local'),
    path('getform/', views.getform, name='getForm'),
    path('rawform/', views.rawform, name='rawform'),
    path('gettest/<int:pk>/', views.gettest, name='gettest'),
    path('gettest2/<str:name>/', views.gettest2, name='gettest2'),
    path('getall/', views.gettestall, name='getall'),
    path('classform/', views.ClassCreate.as_view(), name='ClassCreate'),
    path('classgetall/', views.ClassGetAll.as_view(), name='ClassGetAll'),
    path('classget/<int:pk>/', views.ClassGet.as_view(), name='ClassGet'),
    path('classget2/<str:name>/', views.ClassGet2.as_view(), name='ClassGet2'),
    path('classupdate/<int:pk>/', views.ClassUpdate.as_view(), name='ClassUpdate'),
    path('classdelete/<int:pk>/', views.ClassDelete.as_view(), name='ClassDelete'),
]
