from django.shortcuts import render
from .forms import contactform


def contact_page(request):
    if request.method == 'post':
        form = contactform(request.post)
        if form.is_valid():
            form.save()
    form = contactform()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
