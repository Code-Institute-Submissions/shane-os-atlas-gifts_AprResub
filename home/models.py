""" Home Content Model """
from django.db import models


class Home(models.Model):

    title = models.CharField(max_length=200)
    main_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
