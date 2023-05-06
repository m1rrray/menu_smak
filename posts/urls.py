from django.contrib import admin
from django.urls import path, include
from .views import index
from django.contrib.flatpages import views as views_flat


urlpatterns = [
    # path('dish_modal/<int:dish_id>/', dish_modal, name='dish_modal'),
    path('', index, name='index'),
]