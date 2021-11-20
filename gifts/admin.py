""" Gifts Administration"""
from django.contrib import admin
from .models import Gift, Category


class GiftsAdmin (admin.ModelAdmin):
    """ Gifts Model Administration """
    pass


class CategoryAdmin (admin.ModelAdmin):
    """ Gifts Category Administration """
    pass


admin.site.register(Gift, GiftsAdmin)
admin.site.register(Category, CategoryAdmin)
