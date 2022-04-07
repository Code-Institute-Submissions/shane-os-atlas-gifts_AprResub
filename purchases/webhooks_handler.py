""" Stripe Payments Webhook Handler """
import json
import time
from django.http import HttpResponse
from gifts.models import Gift
from .models import Purchase, LineItem
from profiles.models import UserAccount


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
        billing_details = payment_intent.charges.data[0].billing_details
        shipping = payment_intent.shipping
        grand_total = round(payment_intent.charges.data[0].amount/100, 2)

        for field, value in shipping.address.items():
            if value == "":
                shipping.address[field] = None

        account = None
        username = payment_intent.metadata.username
        if username != 'Anonymous':
            account = UserAccount.objects.get(user=username)
            if profile_info:
                account.official_phone = shipping.phone
                account.official_address_line1 = shipping.address.line1
                account.official_address_line2 = billing_details.address.line2
                account.official_address_line3 = billing_details.address.state
                account.official_town = shipping.address.city
                account.official_country = shipping.address.country
                account.official_postcode = shipping.address.postal_code
                account.save()

        purchase_exists = False
        chance = 1
        while chance < 6:
            try:
                purchase = Purchase.objects.get(
                    name__iexact=shipping.name,
                    phone__iexact=shipping.phone,
                    email__iexact=billing_details.email,
                    address_line1__iexact=shipping.address.line1,
                    address_line2__iexact=billing_details.address.line2,
                    address_line3__iexact=billing_details.address.state,
                    town__iexact=shipping.address.city,
                    country__iexact=shipping.address.country,
                    postcode__iexact=shipping.address.postal_code,
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
                    name=shipping.name,
                    account_profile=account,
                    phone=shipping.phone,
                    email=billing_details.email,
                    address_line1=shipping.address.line1,
                    address_line2=shipping.address.line2,
                    address_line3=shipping.address.state,
                    town=shipping.address.city,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    unique_cart=cart,
                    stripe_paymentid=payment_id,
                )
                for gift_id, quantity in json.loads(cart).items():
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
                    response=f'Stripe Unhandled Webhook Received: {event["type"]} | Error: {e}',
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
