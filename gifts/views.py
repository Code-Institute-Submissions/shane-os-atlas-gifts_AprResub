from django.shortcuts import render
from .models import gifts

def gifts_list_all(request):
    gift = gifts.objects.all()
    context = {
        "gifts": gift,
    }
    return render(request, 'gifts.html', context)
