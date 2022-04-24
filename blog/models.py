""" Blog Post Model Imports """
from django.db import models


class Category(models.Model):

    class Meta:
        """Plural of categories corrected in admin panel """
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=25)


class Post(models.Model):
    """ Blog Post Model """
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category', related_name='posts')
    created_by = models.CharField(max_length=25)
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.title
