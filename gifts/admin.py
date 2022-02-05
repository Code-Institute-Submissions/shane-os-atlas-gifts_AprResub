""" Gifts Administration"""
from django.contrib import admin
from .models import Gift, Category


class GiftsAdmin (admin.ModelAdmin):
    """ Gifts Model Administration """
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'weight',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin (admin.ModelAdmin):
    """ Gifts Category Administration """
    list_display = (
        'name',
        'show_name',
    )

    ordering = ('name',)


admin.site.register(Gift, GiftsAdmin)
admin.site.register(Category, CategoryAdmin)
