""" Gifts app url path """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gifts_list_all, name='gifts'),
    path('add/', views.add_gift, name='add_gift')
]
