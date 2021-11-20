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

    if not stripe_public_key:
        messages.warning(request, 'The Stripe public key is not present!')
    
    purchase_form = PurchaseForm()
    template = 'purchases.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': payment_intent.client_secret,
    }

    return render(request, template, context)
