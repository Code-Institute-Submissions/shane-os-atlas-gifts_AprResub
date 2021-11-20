""" Purchases app views """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe
from cart.context import cart_items
from .forms import PurchaseForm


def order_payment(request):
    """ Display payments form page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty! Please see our gift collection to see our exciting range!")
        return redirect(reverse('gifts'))
    # return render(request, 'purchases.html')

    cart_now = cart_items(request)
    total_now = cart_now['total']
    stripe_total_integer = round(total_now * 100)
    stripe.api_key = stripe_secret_key

    payment_intent = stripe.PaymentIntent.create(
        amount=stripe_total_integer,
        currency=settings.STRIPE_CURRENCY,
    )

    print(payment_intent)
    purchase_form = PurchaseForm()
    template = 'purchases.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': 'pk_test_51Juj7LKooPpz86Xd7dl8QqcG1FLEIJ381EI3Gd4lscP8qCi2UpwlQawesSNokJam6I5cFHqBogIyhGiq1W60ttp5005y7hbcjb',
        'stripe_secret_key': 'secret_key',
    }

    return render(request, template, context)
