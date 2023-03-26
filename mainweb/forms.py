from django.forms import ModelForm
from django import forms
from .models import sendUsMessage

class ContactForm(ModelForm):
    class Meta:
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter your name!"}),
			"email":forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter your Email!"}),
            "subject":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter subject!"}),
			"massege":forms.Textarea(attrs={"class":"form-control", "placeholder":"Enter your messages!","rows":"3"}),
        }
        model = sendUsMessage
        fields = ['name', 'email','subject','massege']
