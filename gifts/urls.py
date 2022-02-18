""" Gifts app url path """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gifts_list_all, name='gifts'),
    path('add/', views.add_gift, name='add_gift'),
    path('edit/<int:gift_id>/', views.edit_gift, name='edit_gift'),
    path('delete/<int:gift_id>/', views.delete_gift, name='delete_gift')
]
