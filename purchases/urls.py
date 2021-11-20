""" Purchases app url path """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_payment, name='purchases')
]
