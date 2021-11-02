from django.shortcuts import render

# Create your views here.

def display_cart(request):

    return render(request, 'cart/cart.html')


def cart_item_add(request, gift_sku):

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if gift_sku in list(cart.keys()):
        cart[gift_sku] += quantity
    else:
        cart[gift_sku] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
