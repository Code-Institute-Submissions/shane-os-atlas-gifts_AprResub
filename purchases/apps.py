""" Purchases app configuration """
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    """ Purchases app name """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchases'

    def change(self):
        """ Import signals file """
        import purchases.signals
