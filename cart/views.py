""" Cart App Views"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Create your views here.


def display_cart(request):
    """ Display cart page """
    return render(request, 'cart/cart.html')


def cart_item_add(request, gift_id):
    """ Add gift to cart """
    quantity = int(request.POST.get('quantity'))
    url_redirect = request.POST.get('url_redirect')
    print(url_redirect)
    cart = request.session.get('cart', {})

    if gift_id in list(cart.keys()):
        cart[gift_id] += quantity
        messages.success(request, "You have increased the gift quantity!")
    else:
        cart[gift_id] = quantity
        messages.success(request, "You have added an item to your cart!")

    request.session['cart'] = cart
    print(request.session['cart'])
    messages.success(request, "You have added an item to your cart!")
    return redirect(url_redirect)


def cart_item_subtract(request, gift_id):
    """ Remove gift remove cart """
    cart = request.session.get('cart', {})

    cart.pop(gift_id)
    messages.success(request, "You have removed an item from your cart!")

    request.session['cart'] = cart
    return redirect(reverse("display_cart"))
