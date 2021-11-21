""" Purchases app views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe
from cart.context import cart_items
from .forms import PurchaseForm
from gifts.models import Gift
from .models import Purchase,LineItem


def order_payment(request):
    """ Display payments form page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        data = {
            'name': request.POST['name'],
            'phone': request.POST['phone'],
            'email': request.POST['Name'],
            'address_line1': request.POST['address_line1],
            'address_line2': request.POST['address_line2'],
            'address_line3': request.POST['address_line3'],
            'town': request.POST['town'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        purchase_form = PurchaseForm(data)
        if purchase_form.is_valid():
            purchase = purchase_form.save()
                for gift_id, quantity in cart.items():
                    gift = get_object_or_404(Gift, pk=gift_id)
                    total += gift.price * quantity
                    gift_count += quantity
                    select_gifts.append({
                        'gift_id': gift_id,
                        'quantity': quantity,
                        'gift': gift,
                    })
                request.session['info'] = 'info' in request.POST
                return redirect(reverse('purchases_success', args=[purchase.order_number]))
        else:
            messages.error(request, "Error! Form filled in incorrectly!")
    else:
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

def purchases_success(request, order_number):
    info = request.session.get('info')
    customer_order = get_object_or_404(Purchase, order_number=order_number)
    messages.success(request, f'Your order was successful! \
                    Order Number: {order_number}.')
    if 'cart' in request.session:
        del request.session['cart']
    
    template = 'purchases_success.html'
    context = {
        'customer_order': customer_order,
    }

    return render(request, template, context)