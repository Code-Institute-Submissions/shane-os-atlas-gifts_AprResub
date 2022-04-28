""" Blog Post Model Imports """
from django.db import models


class Post(models.Model):
    """ Blog Post Model """
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=25)
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.title
