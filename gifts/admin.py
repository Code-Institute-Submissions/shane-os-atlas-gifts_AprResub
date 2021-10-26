from django.contrib import admin
from .models import Gift, Category

class GiftsAdmin (admin.ModelAdmin):
    pass


class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(Gift, GiftsAdmin)
admin.site.register(Category, CategoryAdmin)
