""" Stripe Payments Webhook Handler """
import json
import time
from django.http import HttpResponse
from gifts.models import Gift
from .models import Purchase, LineItem


class StripeWebhookHandler:
    """ Stripe Webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Unexpected event handling """
        return HttpResponse(
            response=f'Stripe Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Stripe payment_intent_succeeded webhook handling """
        print('success')

        payment_intent = event.data.objects
        print(payment_intent)
        payment_id = payment_intent.id
        cart = payment_intent.metadata.cart
        profile_info = payment_intent.metadata.profile_info
        payment_details = payment_intent.charges.data[0].payment_details
        delivery_details = payment_intent.delivery_details
        grand_total = round(payment_intent.charges.data[0].amount/100, 2)

        for field, value in delivery_details.recipient_address.items():
            if value == "":
                delivery_details.recipient_address[field] = None

        purchase_exists = False
        chance = 1
        while chance < 6:
            try:
                purchase = Purchase.objects.get(
                    name__iexact=delivery_details.name,
                    phone__iexact=delivery_details.phone,
                    email__iexact=payment_details.phone,
                    address_line1__iexact=delivery_details.address_line1,
                    address_line2__iexact=payment_details.address_line2,
                    address_line3__iexact=payment_details.address_line3,
                    town__iexact=delivery_details.town,
                    country__iexact=delivery_details.country,
                    postcode__iexact=delivery_details.postcode,
                    grand_total=grand_total,
                    unique_cart=cart,
                    stripe_paymentid=payment_id,
                )
                purchase_exists = True
                break

            except Purchase.DoesNotExist:
                chance += 1
                time.sleep(1)
        if purchase_exists:
            return HttpResponse(
                response=f'Stripe Webhook Received: {event["type"]}| Order already exists in Database',
                status=200)
        else:
            purchase = None
            try:
                purchase = Purchase.objects.create(
                    name=delivery_details.name,
                    phone=delivery_details.phone,
                    email=payment_details.phone,
                    address_line1=delivery_details.address_line1,
                    address_line2=payment_details.address_line2,
                    address_line3=payment_details.address_line3,
                    town=delivery_details.town,
                    country=delivery_details.country,
                    postcode=delivery_details.postcode,
                    unique_cart=cart,
                    stripe_paymentid=payment_id,
                )
                for gift_id, quantity in json.loads(cart).items:
                    gift = Gift.objects.get(id=gift_id)
                    purchase_line_item = LineItem(
                        purchase=purchase,
                        gift=gift,
                        quantity=quantity,
                    )
                    purchase_line_item.save()
            except Exception as e:
                if purchase:
                    purchase.delete()
                return HttpResponse(
                    response=f'Stripe Unhandled Webhook Received: {event["type"]} | Error {e}',
                    status=500)

        return HttpResponse(
            response=f'Stripe Unhandled Webhook Received: {event["type"]} | Order Created',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Stripe payment_intent_payment_failed webhook handling  """
        return HttpResponse(
            response=f'Stripe Webhook Received: {event["type"]}',
            status=200
        )
