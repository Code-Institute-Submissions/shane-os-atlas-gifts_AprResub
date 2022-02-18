from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Gift, Category
from .forms import GiftForm


def gifts_list_all(request):
    """ Show gifts on page """
    gifts = Gift.objects.all()
    searchquery = None
    sortchoice = None
    direction = None
    categorychoice = None

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

            if 'category' in request.GET:
                categorychoice = request.GET['category']
                gifts = gifts.filter(category__name__in=categorychoice)
                categorychoice = Category.objects.filter(name__in=categorychoice)

            if 'q' in request.GET:
                searchquery = request.GET['q']
                if not searchquery:
                    return redirect(reverse('gifts'))
                    messages.error(request, "Incorrect search query! Please try again")

                searchqueries = Q(name__icontains=searchquery) | Q(description__icontains=searchquery)
                gifts = gifts.filter(searchqueries)

    sort_choice = f'{sortchoice}_{direction}'

    context = {
            "gifts": gifts,
            "sort_choice": sort_choice,
            "searchresult": searchquery,
            "category_choice": categorychoice,
    }

    return render(request, 'gifts/gifts.html', context)


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


def edit_gift(request, gift_id):
    """ Edit gift details """
    gift = get_object_or_404(Gift, pk=gift_id)
    form = GiftForm(instance=gift)

    template = 'gifts/edit_gift.html'
    context = {
        'form': form,
        'gift': gift
    }

    return render(request, template, context)
