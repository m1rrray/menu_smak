from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.flatpages import views as views_flat


urlpatterns = [
    path('', views.index, name='index')
]