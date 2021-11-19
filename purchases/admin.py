from django.contrib import admin
from .models import Purchase, LineItem


class PurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'total',)

    fields = ('name', 'phone', 'email', 'address_line1',
                 'address_line2', 'address_line3', 'town', 'postcode',
                 'country', 'order_number', 'date', 'total',)

    list_display = ('order_number', 'date', 'name', 'email', 'total',)

admin.site.register(Purchase, PurchaseAdmin)
