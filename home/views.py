""" Home app view """
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from home.models import Home
from home.forms import HomeForm


def index(request):
    """ Home page display """
    welcome = Home.objects.all()

    context = {
        "welcomes": welcome,
    }

    return render(request, 'home/index.html', context)


def add_home(request):
    """ Add Home Page Content """
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect('home')
    else:
        form = HomeForm()

    context = {
        "form": form
    }

    return render(request, 'home/add_home.html', context)
