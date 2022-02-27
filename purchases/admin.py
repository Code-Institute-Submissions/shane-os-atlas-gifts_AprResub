""" Purchases app administration """
from django.contrib import admin
from .models import Purchase, LineItem


class LineItemAdminInLine(admin.TabularInline):
    """ Line items administration """
    model = LineItem
    readonly_fields = ('sub_total',)


class PurchaseAdmin(admin.ModelAdmin):
    """ Site Purchases Admin """
    inlines = (LineItemAdminInLine,)
    """ Purchases form administration """
    readonly_fields = ('order_number', 'date', 'pre_discount_total',
                       'discount', 'final_total')

    fields = ('name', 'phone', 'email', 'address_line1',
              'address_line2', 'address_line3', 'town', 'postcode',
              'country', 'order_number', 'date', 'pre_discount_total',)

    list_display = ('order_number', 'date', 'name', 'email',
                    'pre_discount_total',)

    ordering = ('-date',)


admin.site.register(Purchase, PurchaseAdmin)
