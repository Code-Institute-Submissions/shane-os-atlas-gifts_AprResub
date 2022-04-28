""" Gift App Imported Modules """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Gift
from .forms import GiftForm


def gifts_list_all(request):
    """ Show gifts on page """
    gifts = Gift.objects.all()
    searchquery = None
    sortchoice = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortchoice = request.GET['sort']
            sort = sortchoice
            if sortchoice == 'name':
                sortchoice = 'lower_name'
                gifts = gifts.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortchoice = f'-{sort}'
            gifts = gifts.order_by(sortchoice)

        if 'q' in request.GET:
            searchquery = request.GET['q']
            if not searchquery:
                messages.error(request,
                               "Incorrect search query! Please try again")
                return redirect(reverse('gifts'))

            searchqueries = Q(name__icontains=searchquery) | Q(description__icontains=searchquery)
            gifts = gifts.filter(searchqueries)
            if gifts:
                print("I'm Full")
            else:
                print("I'm Empty")
                gifts = Gift.objects.all()
                messages.error(request,
                               "Incorrect search query! Please try again")

    sort_choice = f'{sortchoice}_{direction}'

    context = {
            "gifts": gifts,
            "sort_choice": sort_choice,
            "searchresult": searchquery,
    }

    return render(request, 'gifts/gifts.html', context)


@login_required
def add_gift(request):
    """ Add a new gift """
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, "A new gift has been added!")
            return redirect(reverse('add_gift'))
        else:
            messages.error(request, "Error: Gift not added!")
    else:
        form = GiftForm()
    form = GiftForm()
    template = 'gifts/add_gift.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_gift(request, gift_id):
    """ Edit gift details """
    gift = get_object_or_404(Gift, pk=gift_id)
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES, instance=gift)
        if form.is_valid():
            form.save()
            messages.success(request, "Gift information successfully updated!")
            return redirect(reverse('gifts'))
        else:
            messages.error(request,
                           "Form is not valid. Please check and try again.")
    form = GiftForm(instance=gift)

    template = 'gifts/edit_gift.html'
    context = {
        'form': form,
        'gift': gift
    }

    return render(request, template, context)


@login_required
def delete_gift(request, gift_id):
    """ Delete Gift from Website """
    gift = get_object_or_404(Gift, pk=gift_id)
    gift.delete()
    messages.success(request, "Gift successfully deleted!")
    return redirect(reverse('gifts'))
