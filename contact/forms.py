""" Contact App Form """
from django import forms
from .models import Contact


class contactForm(forms.ModelForm):
    """ Contact Form for Visitors """
    class Meta:
        """ Contact Meta Class Fields """
        model = Contact
        fields = ('name', 'subject', 'from_email', 'message',)
