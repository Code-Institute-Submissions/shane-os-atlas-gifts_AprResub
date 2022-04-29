""" Purchases form """
from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    """ Purchases form creation """
    class Meta:
        """ Purchases form fields """
        model = Purchase
        fields = (
            'name', 'phone', 'email', 'address_line1',
            'address_line2', 'address_line3', 'town', 'postcode',
            'country',
            )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        titles = {
            'name': 'Name',
            'phone': 'Phone Number (Include Area Code)',
            'email': 'Email Address',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'address_line3': 'Address Line 3',
            'town': 'Town',
            'postcode': 'Eircode(Postcode)',
            'country': 'Country',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                title = f'{titles[field]} *'
            else:
                title = titles[field]
            self.fields[field].widget.attrs['title'] = title
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
