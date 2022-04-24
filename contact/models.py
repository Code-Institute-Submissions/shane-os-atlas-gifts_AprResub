""" Contact App Model Import """
from django.db import models


class Contact(models.Model):
    """ Contact App Model """
    name = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    from_email = models.EmailField(max_length=128, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.name
