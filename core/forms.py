from django.forms import ModelForm
from core.models import ContactRequest



class ContactRequestForm(ModelForm):
    """Form definition for RentRequest."""

    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message', 'phone')

