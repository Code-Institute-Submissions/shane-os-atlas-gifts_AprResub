from django.conf import settings
from django.http import HttpResponse
from purchases.webhook_handler import StripeWebhookHandler
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """ Receive Stripe Webhooks """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(response=e, status=400)
    
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print("Payment Intent was Successful!")
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object
        print("Payment Method was attached to a Customer!")
    else:
        return HttpResponse(status=400)
    
    return HttpResponse(status=200)