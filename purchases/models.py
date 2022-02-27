""" Purchases app models """
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from gifts.models import Gift
from profiles.models import UserAccount


class Purchase(models.Model):
    """ Purchase Model - User Details Fields"""
    account_profile = models.ForeignKey(UserAccount, on_delete=models.SET_NULL,
                                        null=True, blank=True,
                                        related_name='purchases')
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
    pre_discount_total = models.DecimalField(max_digits=7, decimal_places=2,
                                             null=False, default=0)
    discount = models.DecimalField(max_digits=7, decimal_places=2,
                                   null=False, default=0)
    final_total = models.DecimalField(max_digits=7, decimal_places=2,
                                      null=False, default=0)

    def _create_order_number(self):
        """ Create unique order number """
        return uuid.uuid4().hex.upper()

    def total(self):
        """ Calculate total after applying delivery and discounts """
        self.pre_discount_total = self.item_purchase.aggregate(Sum('sub_total'))['sub_total__sum'] or 0
        if self.pre_discount_total > settings.DISCOUNT_THRESHOLD:
            self.discount = self.pre_discount_total * settings.DISCOUNT_RATE / 100
        else:
            self.discount = 0
        delivery_charge = settings.DELIVERY_CHARGE
        self.final_total = self.pre_discount_total - self.discount + delivery_charge
        self.save()

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

    def __str__(self):
        return f'Order Number: {self.purchase.order_number}'
