""" Creates url pattern for blog posts"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_id, name='blog'),
    path('create/', views.create_blog, name='create_blog')
]
