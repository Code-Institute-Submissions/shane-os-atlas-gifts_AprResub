""" App to calculate line item sub totals"""
from django import template

register = template.Library()


@register.filter(name='gift_subtotal')
def gift_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal
