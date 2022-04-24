""" Contact Form App Imported Modules """
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .models import Contact
from .forms import contactForm


def contact_page(request):
    """ Site Contact Form """
    if request.method == 'GET':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [from_email, settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid Entry')
            messages.success(request,
                             "Contact Form Submitted! \
                             Thank you for your message. We will be in touch soon!")
            return redirect(reverse('home'))

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return HttpResponse('Thank you!')
