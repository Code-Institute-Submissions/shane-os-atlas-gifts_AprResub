""" User Account """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from purchases.models import Purchase


def profile(request):
    """ Show User Account """

    profile = get_object_or_404(UserAccount, user=request.user)

    if request.method == "POST":
        profile_update = UserAccountForm(request.POST, instance=profile)
        if profile_update.is_valid():
            profile_update.save()
            messages.success(request, "Your profile was saved successfully!")

    form = UserAccountForm(instance=profile)
    past_purchases = profile.purchases.all()
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'past_purchases': past_purchases,
    }

    return render(request, template, context)


def purchase_history(request, order_number):
    """ Show User Purchase History """
    purchase = get_object_or_404(Purchase, order_number=order_number)

    messages.info(request, (
        f'Order: {order_number} has already taken place.'
        'You are viewing the historical record.'
    ))

    template = 'purchases/purchases_success.html'
    context = {
        'customer_order': purchase,
    }

    return render(request, template, context)
