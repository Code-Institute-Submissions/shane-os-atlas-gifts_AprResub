""" Profiles form """
from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    """ Profiles form creation """
    class Meta:
        """ Profiles form fields """
        model = UserAccount
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        titles = {
            'official_phone': 'Phone Number (Include Area Code)',
            'official_address_line1': 'Address Line 1',
            'official_address_line2': 'Address Line 2',
            'official_address_line3': 'Address Line 3',
            'official_town': 'Town',
            'official_postcode': 'Eircode(Postcode)',
            'official_country': 'Country',
        }

        self.fields['official_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                title = f'{titles[field]} *'
            else:
                title = titles[field]
            self.fields[field].widget.attrs['title'] = title
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
