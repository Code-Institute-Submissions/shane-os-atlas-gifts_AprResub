""" User Account """
from django.shortcuts import render, get_object_or_404
from .models import UserAccount
from .forms import UserAccountForm


def profile(request):
    """ Show User Account """
    print(request)
    profile = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)
