from django.contrib import admin
from django.urls import path, re_path, include
from user import views

urlpatterns = [
    re_path(r'^$', views.index,name = 'index')
]
