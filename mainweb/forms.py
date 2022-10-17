from django.forms import ModelForm
from .models import sendUsMessage

class ContactForm(ModelForm):
    class Meta:
        model = sendUsMessage
        fields = ['name', 'email','subject','massege']
