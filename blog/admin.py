""" Blog App Administration """
from django.contrib import admin
from blog.models import Post


class BlogAdmin (admin.ModelAdmin):
    """ Blog App Admin """
    pass


admin.site.register(Post, BlogAdmin)
