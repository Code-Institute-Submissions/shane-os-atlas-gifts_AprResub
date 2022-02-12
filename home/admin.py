""" Home Page Text Administration """
from django.contrib import admin
from .models import Home
# Register your models here.

class HomeAdmin (admin.ModelAdmin):
    """ Home Model Administration """
    list_display = (
        'title',
        'main_text',
    )

    ordering = ('title',)


admin.site.register(Home, HomeAdmin)
