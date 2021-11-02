from django.shortcuts import render, redirect

# Create your views here.


def display_cart(request):

    return render(request, 'cart/cart.html')


def cart_item_add(request, gift_sku):

    quantity = int(request.POST.get('quantity'))
    url_redirect = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if gift_sku in list(cart.keys()):
        cart[gift_sku] += quantity
    else:
        cart[gift_sku] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(url_redirect)
