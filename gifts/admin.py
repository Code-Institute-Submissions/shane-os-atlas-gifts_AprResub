""" Gifts Administration"""
from django.contrib import admin
from .models import Gift


class GiftsAdmin (admin.ModelAdmin):
    """ Gifts Model Administration """
    list_display = (
        'sku',
        'name',
        'price',
        'weight',
        'image',
    )

    ordering = ('name',)


admin.site.register(Gift, GiftsAdmin)
