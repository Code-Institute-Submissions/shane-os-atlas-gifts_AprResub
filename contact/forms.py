from django import forms
from .models import Contact


class contactForm(forms.ModelForm):
    """ Contact Form for Visitors """
    class Meta:
        model = Contact
        fields = ('name', 'subject', 'from_email', 'message',)
