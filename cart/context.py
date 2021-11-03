from django.conf import settings
from django.shortcuts import get_object_or_404
from gifts.models import Gift


def cart_items(request):

    select_gifts = []
    gift_count = 0
    total = 0
    cart = request.session.get('cart', {})

    for gift_id, quantity in cart.items():
        gift = get_object_or_404(Gift, pk=gift_id)
        total = gift.price * quantity
        gift_count += quantity
        select_gifts.append({
            'gift_id': gift_id,
            'quantity': quantity,
            'gift': gift,
        })


    context = {
        'select_gifts': select_gifts,
        'gift_count': gift_count,
        'total': total,
    }

    return context
