""" Add a Gift Required Modules """
from django import forms
from .models import Gift, Category


class GiftForm(forms.ModelForm):
    """ Add a Gift Form"""
    class Meta:
        model = Gift
        fields = '__all__'
