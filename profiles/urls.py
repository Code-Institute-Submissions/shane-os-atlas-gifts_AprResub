""" Creates url pattern for user account"""
from django.urls import path
from profiles.views import profile

urlpatterns = [
    path('', profile, name='profile'),
]
