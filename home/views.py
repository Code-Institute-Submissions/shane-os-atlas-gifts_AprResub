""" Home app view """
from django.shortcuts import render


def index(request):
    """ Home page display """
    return render(request, 'home/index.html')
