""" Add a Gift Required Modules """
from django import forms
from .models import Gift


class GiftForm(forms.ModelForm):
    """ Add a Gift Form"""
    class Meta:
        """ Gift Model """
        model = Gift
        fields = '__all__'
