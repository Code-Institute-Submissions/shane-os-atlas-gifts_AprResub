""" Contact Form App Imported Modules """
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Contact
from .forms import contactform


def contact_page(request):
    if request.method == 'GET':
        form = contactform()
    else:
        form = contactform(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'info@atlasgifts.com', [email])
            except BadHeaderError:
                return HttpResponse('Invalid Entry')
            return redirect('contact_success')

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return HttpResponse('Thank you!')
