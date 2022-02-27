""" Stripe Payments Webhook Handler """
from django.http import HttpResponse


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
        return HttpResponse(
            response=f'Stripe Unhandled Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Stripe payment_intent_payment_failed webhook handling  """
        return HttpResponse(
            response=f'Stripe Webhook Received: {event["type"]}',
            status=200
        )
