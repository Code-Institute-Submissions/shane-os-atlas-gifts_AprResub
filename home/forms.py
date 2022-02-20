""" Add Home Page Content """
from django import forms
from .models import Home


class HomeForm(forms.ModelForm):
    """ Form to add home page content """
    class Meta:

        model = Home
        fields = ('title', 'main_text',)
