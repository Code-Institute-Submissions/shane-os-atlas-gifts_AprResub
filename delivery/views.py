from django.shortcuts import render

# Create your views here.


def delivery_tracker(request):

    return render(request, 'delivery.html')
