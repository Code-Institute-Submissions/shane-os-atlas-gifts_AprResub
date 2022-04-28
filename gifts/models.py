""" Import models from Django """
from django.db import models


class Gift(models.Model):
    """ Gifts Model """
    class Meta:
        """ Plural of Gift shown in admin panel """
        verbose_name_plural = "Gifts"

    sku = models.CharField(max_length=25)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=3, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_sku(self):
        """ Returns stock keeping unit id """
        return self.sku
