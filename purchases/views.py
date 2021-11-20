from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseForm
from cart.context import cart_items
import stripe
from django.conf import settings
# Create your views here.


def order_payment(request):

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty! Please see our gift collection to see our exciting range!")
        return redirect(reverse('gifts'))
    # return render(request, 'purchases.html')

    cart_now = cart_items(request)
    total_now = cart_now['total']
    stripe_total_integer = round(total_now * 100)
    purchase_form = PurchaseForm()
    template = 'purchases.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': 'pk_test_51Juj7LKooPpz86Xd7dl8QqcG1FLEIJ381EI3Gd4lscP8qCi2UpwlQawesSNokJam6I5cFHqBogIyhGiq1W60ttp5005y7hbcjb',
        'stripe_secret_key': 'secret_key',
    }

    return render(request, template, context)
