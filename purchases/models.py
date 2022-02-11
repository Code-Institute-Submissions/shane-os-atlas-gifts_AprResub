""" Purchases app models """
import uuid

from django.db import models
from django.db.models import Sum
from gifts.models import Gift
from django.conf import settings


class Purchase(models.Model):
    """ Purchase Model - User Details Fields"""
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=128, null=False, blank=False)
    address_line1 = models.CharField(max_length=100, null=False, blank=False)
    address_line2 = models.CharField(max_length=100, null=False, blank=True)
    address_line3 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, null=False,
                                default=0)

    def _create_order_number(self):
        """ Create unique order number """
        return uuid.uuid4().hex.upper()

    def final_total(self):
        self.total = self.item_purchase.aggregate(Sum('sub_total'))

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class LineItem (models.Model):
    purchase = models.ForeignKey(Purchase, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='item_purchase')
    gift = models.ForeignKey(Gift, null=False, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    sub_total = models.DecimalField(max_digits=5, decimal_places=2, null=False,
                                    blank=False, editable=False)

    def save(self, *args, **kwargs):

        self.sub_total = self.gift.price * self.quantity
        super().save(*args, **kwargs)
