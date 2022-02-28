""" Home Page Text Administration """
from django.contrib import admin
from .models import Home


class HomeAdmin (admin.ModelAdmin):
    """ Home Model Administration """
    list_display = (
        'title',
        'main_text',
    )

    ordering = ('title',)


admin.site.register(Home, HomeAdmin)
