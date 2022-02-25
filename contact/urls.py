""" Create URL patter for contact form """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_page, name='contact_page'),
    path('', views.contact_success, name='contact_success')
]
