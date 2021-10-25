from django.contrib import admin
from .models import gifts, Category

class GiftsAdmin (admin.ModelAdmin):
    pass


class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(gifts, GiftsAdmin)
admin.site.register(Category, CategoryAdmin)
