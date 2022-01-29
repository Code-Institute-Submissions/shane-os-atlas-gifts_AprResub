from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Gift


def gifts_list_all(request):
    """ Show gifts on page """
    gift = Gift.objects.all()
    searchquery = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortoption = request.GET['sort']
            sort = sortoption

            if sortoption == 'name':
                sortoption = 'lower_name'
                gift = gift.annotate(lower_name = Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortoption = f'-{sortoption}'
            gift = gift.order_by(sortoption)

            if 'q' in request.GET:
                searchquery = request.GET['q']
                if not searchquery:
                    return redirect(reverse('gifts'))
                    messages.error(request, "Incorrect search query! Please try again")

                searchqueries = Q(name__icontains=searchquery) | Q(description__icontains=searchquery)
                gift = gift.filter(searchqueries)

    sort_choice = f'{sort}_{direction}'

    context = {
            "gifts": gift,
            "sort_choice": sort_choice,
            "searchresult": searchquery,
    }

    return render(request, 'gifts/gifts.html', context)
