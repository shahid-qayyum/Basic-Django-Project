from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import address

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True,label=('Email'))
    class Meta:
        model=User
        fields=("username","email","password1","password2")

class contactview(forms.Form):
    name= forms.CharField(max_length=255)
    email= forms.EmailField()
    subject= forms.CharField(max_length=255)
    message= forms.CharField(widget=forms.Textarea)

class checkoutform(forms.ModelForm):
    class Meta:
        model=address
        fields=("street_address","state","zip","country","phone")