""" Cart App URL Path"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add/<gift_id>/', views.cart_item_add, name='cart_item_add'),
    path('remove/<gift_id>/', views.cart_item_subtract,
         name='cart_item_subtract')
]
