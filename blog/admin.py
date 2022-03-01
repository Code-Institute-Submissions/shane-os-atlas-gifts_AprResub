""" Blog App Administration """
from django.contrib import admin
from blog.models import Post, Category


class BlogAdmin (admin.ModelAdmin):
    pass


class CategoryAdmin (admin.ModelAdmin):
    pass


admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
