""" Blog App Configuration """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Blog App Name """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
