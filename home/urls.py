from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_home, name='add_home'),
    path('edit/<int:home_id>/', views.edit_home, name='edit_home')
]
