from django.db import models

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
