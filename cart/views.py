from django.shortcuts import render

# Create your views here.

def display_cart(request):

    return render(request, 'cart/cart.html')
