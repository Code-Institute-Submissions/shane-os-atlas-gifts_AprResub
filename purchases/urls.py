""" Purchases app url path """
from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.order_payment, name='purchases'),
    path('purchases_success/<order_number>', views.purchases_success, name='purchases_success'),
    path('wh/', webhook, name='webhook'),
]
