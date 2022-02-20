""" Creates url pattern for blog posts"""
from django.urls import path
from blog.views import blog_show, create_post, edit_blog

urlpatterns = [
    path('', blog_show, name='blog'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog')
]
