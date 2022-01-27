from django.shortcuts import render
from .models import Gift


def gifts_list_all(request):
    """ Show gifts on page """
    gift = Gift.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortoption = request.GET['sort']
            sort = sortoption

            if sortoption == 'name':
                sortoption = 'lower_name'
                gift = gift.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortoption = f'-{sortoption}'
            gift = gift.order_by(sortoption)

    sort_choice = f'{sort}_{direction}'

    context = {
            "gifts": gift,
            "sort_choice": sort_choice,
    }
    return render(request, 'gifts/gifts.html', context)
