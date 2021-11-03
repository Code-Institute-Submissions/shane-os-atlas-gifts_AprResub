from django.shortcuts import render, redirect

# Create your views here.


def display_cart(request):

    return render(request, 'cart/cart.html')


def cart_item_add(request, gift_id):

    quantity = int(request.POST.get('quantity'))
    url_redirect = request.POST.get('url_redirect')
    print(url_redirect)
    cart = request.session.get('cart', {})

    if gift_id in list(cart.keys()):
        cart[gift_id] += quantity
    else:
        cart[gift_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(url_redirect)
