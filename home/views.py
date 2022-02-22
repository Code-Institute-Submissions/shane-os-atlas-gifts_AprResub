""" Home app view """
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import Home
from home.forms import HomeForm


def index(request):
    """ Home page display """
    welcome = Home.objects.all()

    context = {
        "welcomes": welcome,
    }

    return render(request, 'home/index.html', context)


@login_required
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


@login_required
def edit_home(request, home_id):
    """ Edit Gome Content """
    welcome = get_object_or_404(Home, id=home_id)
    if request.method == 'POST':
        form = HomeForm(request.POST, instance=welcome)
        if form.is_valid():
            form.save()
            messages.success(request, "Home page successfully updated!")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Error: Home page update was unsuccessful! Please check the form and try again.")
    form = HomeForm(instance=welcome)

    template = 'home/edit_home.html'
    context = {
        'form': form,
        'welcome': welcome
    }
    return render(request, template, context)


@login_required
def delete_home(request, home_id):
    """ Delete Home Content """
    welcome = get_object_or_404(Home, pk=home_id)
    welcome.delete()
    messages.success(request, "Home content successfully deleted!")
    return redirect(reverse('home'))
