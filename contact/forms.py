from django import forms
from .models import Contact


class contactform(forms.ModelForm):
    """ Contact Form for Visitors """
    class Meta:
        model = Contact
        fields = ('name', 'subject', 'email', 'message',)
