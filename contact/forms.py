from django.forms import ModelForm
from .models import Contact

class contactform(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
