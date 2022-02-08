from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from gifts.models import Gift


def cart_items(request):
    """ Gifts saved in cart """
    select_gifts = []
    gift_count = 0
    total = 0
    cart = request.session.get('cart', {})

    for gift_id, quantity in cart.items():
        gift = get_object_or_404(Gift, pk=gift_id)
        total += gift.price * quantity
        gift_count += quantity
        select_gifts.append({
            'gift_id': gift_id,
            'quantity': quantity,
            'gift': gift,
        })

    if total > settings.DISCOUNT_THRESHOLD:
        discount_rate = Decimal(settings.DISCOUNT_RATE/100)
        discount_amount = total * discount_rate
        subtotal = total - discount_amount
        subtotal = round(subtotal, 2)
        total = subtotal + settings.DELIVERY_CHARGE
    else:
        total = total + settings.DELIVERY_CHARGE

    context = {
        'select_gifts': select_gifts,
        'gift_count': gift_count,
        'subtotal': subtotal,
        'total': total,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount_rate': settings.DISCOUNT_RATE,
        'delivery': settings.DELIVERY_CHARGE,
    }

    return context
