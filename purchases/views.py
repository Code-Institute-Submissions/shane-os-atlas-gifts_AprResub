""" Purchases app views """
import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe

from cart.context import cart_items
from gifts.models import Gift
from profiles.forms import UserAccountForm
from profiles.models import UserAccount
from .forms import PurchaseForm
from .models import Purchase, LineItem


@require_POST
def purchases_data_cache(request):
    """ Purchase App Cache """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'personal_info': request.POST.get('personal_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        print("EXCEPTION: ", e)
        messages.error(request, "Error! Your payment was not processed! \
            Please try again later.")
        return HttpResponse(content=e, status=400)


def purchases(request):
    """ Display payments form page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    total = 0
    gift_count = 0
    select_gifts = []

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        data = {
            'name': request.POST['name'],
            'phone': request.POST['phone'],
            'email': request.POST['email'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'address_line3': request.POST['address_line3'],
            'town': request.POST['town'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        purchase_form = PurchaseForm(data)
        if purchase_form.is_valid():
            purchase = purchase_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            purchase.stripe_pid = pid
            purchase.unique_cart = json.dumps(cart)
            purchase.save()
            for gift_id, quantity in cart.items():
                try:
                    gift = Gift.objects.get(id=gift_id)
                    purchase_line_item = LineItem(
                        purchase=purchase,
                        gift=gift,
                        quantity=quantity,
                    )
                    purchase_line_item.save()
                    total += gift.price * quantity
                    gift_count += quantity
                    select_gifts.append({
                        'gift_id': gift_id,
                        'quantity': quantity,
                        'gift': gift,
                    })
                except Gift.DoesNotExist:
                    messages.error(request,
                                   "We are very sorry, \
                                       but that item no longer exists.")
                    purchase.delete()
                    return redirect(reverse('view_cart'))

            request.session['personal_info'] = 'personal_info' in request.POST
            return redirect(reverse('purchases_success',
                                    args=[purchase.order_number]))
        else:
            messages.error(request, "Error! Form filled in incorrectly!")
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "Your cart is currently empty! Please see our gift collection to see our exciting range!")
            return redirect(reverse('gifts'))

        cart_now = cart_items(request)
        total_now = cart_now['grandtotal']
        stripe_total_integer = round(total_now * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total_integer,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        if request.user.is_authenticated:
            try:
                info = UserAccount.objects.get(user=request.user)
                purchase_form = PurchaseForm(initial={
                    'name': info.user.get_short_name(),
                    'phone': info.official_phone,
                    'email': info.user.email,
                    'address_line1': info.official_address_line1,
                    'address_line2': info.official_address_line2,
                    'address_line3': info.official_address_line3,
                    'town': info.official_town,
                    'postcode': info.official_postcode,
                    'country': info.official_country,
                })
            except UserAccount.DoesNotExist:
                purchase_form = PurchaseForm()
        else:
            purchase_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'The Stripe public key is not present!')

    template = 'purchases/purchases.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def purchases_success(request, order_number):
    """ Display payment confirmation page """
    personal_info = request.session.get('personal_info')
    customer_order = get_object_or_404(Purchase, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserAccount.objects.get(user=request.user)
        customer_order.account_profile = profile
        customer_order.save()

        if personal_info:
            delivery_info = {
                'official_phone': customer_order.phone,
                'official_address_line1': customer_order.address_line1,
                'official_address_line2': customer_order.address_line2,
                'official_address_line3': customer_order.address_line3,
                'official_town': customer_order.town,
                'official_postcode': customer_order.postcode,
                'official_country': customer_order.country,
            }
            user_personal_info = UserAccountForm(delivery_info, instance=profile)
            if user_personal_info.is_valid():
                user_personal_info.save()

    messages.success(request, f'Your order was successful! \
                    Order Number: {order_number}. Your receipt will be sent to {customer_order.email}')
    if 'cart' in request.session:
        del request.session['cart']

    template = 'purchases/purchases_success.html'
    context = {
        'customer_order': customer_order,
    }

    return render(request, template, context)
