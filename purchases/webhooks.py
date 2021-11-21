from django.http import HttpResponse

class StripeWebhookHandler:
    """ Stripe Webhooks"""
    def __init__(self, request):
        self.request = request

    def event_handle(self, event):
        """ Unexpected event handling """
        return HttpResponse(
            response = f'Stripe Webhook Received: {event["type"]}',
            status=200
        )
