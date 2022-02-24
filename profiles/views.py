""" User Account """
from django.shortcuts import render


def profile(request):
    """ Show User Account """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
