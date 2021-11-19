from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseForm
# Create your views here.


def order_payment(request):

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty! Please see our gift collection to see our exciting range!")
        return redirect(reverse('gifts'))
    return render(request, 'purchases.html')

    purchase_form = PurchaseForm()
    template = 'purchases/purchases.html'
    context = {
        'purchase_form': purchase_form,
    }

    return render(request, template, context)