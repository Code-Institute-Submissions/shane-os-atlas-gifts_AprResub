""" Purchases app url path """
from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.purchases, name='purchases'),
    path('purchases_success/<order_number>', views.purchases_success,
         name='purchases_success'),
    path('purchases_data_cache/', views.purchases_data_cache,
         name='purchases_data_cache'),
    path('wh/', webhook, name='webhook'),
]
