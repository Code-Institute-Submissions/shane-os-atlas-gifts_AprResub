from django.shortcuts import render

# Create your views here.
def order_payment(request):

    return render(request, 'purchases.html')
