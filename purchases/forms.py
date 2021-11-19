from django import forms
from .models import Purchase, LineItem


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('name', 'phone', 'email', 'address_line1',
                    'address_line2', 'address_line3', 'town', 'postcode',
                    'country',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        titles = {'name': 'Name',
                        'phone': 'Phone Number (Include Area Code)',
                        'email': 'Email Address',
                        'address_line1': 'Address Line 1',
                        'address_line2': 'Address Line 2',
                        'address_line3': 'Address Line 3',
                        'town': 'Town',
                        'postcode': 'Eircode(Postcode)',
                        'country': 'Country',
                    }