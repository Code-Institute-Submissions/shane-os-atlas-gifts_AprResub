""" Home app view """
from django.shortcuts import render
from home.models import Home


def index(request):
    """ Home page display """
    welcome = Home.objects.all()

    context = {
        "welcomes": welcome,
    }

    return render(request, 'home/index.html', context)
