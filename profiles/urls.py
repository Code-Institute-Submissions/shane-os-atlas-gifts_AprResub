""" Creates url pattern for user account"""
from django.urls import path
from profiles.views import profile
from profiles.views import purchase_history

urlpatterns = [
    path('', profile, name='profile'),
    path('purchase_history/<order_number>', purchase_history, name='purchase_history'),
]
