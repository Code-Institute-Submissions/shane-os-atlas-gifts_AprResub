""" Cart App URL Path"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add/<gift_id>/', views.cart_item_add, name='cart_item_add'),
    path('change/<gift_id>/', views.change_quantity, name='change_quantity'),
    path('remove/<gift_id>/', views.cart_item_subtract,
         name='cart_item_subtract')
]
