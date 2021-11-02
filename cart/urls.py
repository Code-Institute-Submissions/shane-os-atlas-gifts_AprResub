from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add/<gift_sku>/', views.cart_item_add, name='cart_item_add')
]
