""" Import App """
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """ Contact Form App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
