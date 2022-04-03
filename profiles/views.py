""" User Account """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm


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
