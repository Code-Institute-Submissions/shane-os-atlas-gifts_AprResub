from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from gifts.models import Gift


def cart_items(request):
    """ Gifts saved in cart """
    select_gifts = []
    gift_count = 0
    subtotal = 0
    cart = request.session.get('cart', {})

    for gift_id, quantity in cart.items():
        gift = get_object_or_404(Gift, pk=gift_id)
        subtotal += gift.price * quantity
        gift_count += quantity
        select_gifts.append({
            'gift_id': gift_id,
            'quantity': quantity,
            'gift': gift,
        })

    if subtotal > settings.DISCOUNT_THRESHOLD:
        discount_rate = Decimal(settings.DISCOUNT_RATE/100)
        discount_amount = subtotal * discount_rate
        total = subtotal - discount_amount
        total = round(total, 2)
        grandtotal = total + settings.DELIVERY_CHARGE
    else:
        total = subtotal
        discount_amount = 0
        grandtotal = total + settings.DELIVERY_CHARGE

    context = {
        'select_gifts': select_gifts,
        'gift_count': gift_count,
        'subtotal': subtotal,
        'total': total,
        'grandtotal': grandtotal,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount_rate': settings.DISCOUNT_RATE,
        'discount_amount': discount_amount,
        'delivery': settings.DELIVERY_CHARGE,
    }

    return context
