from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, EmailInput
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = {'client', 'client_email', 'client_phone_number', 'client_address'}

        widgets = {
            'client': TextInput(attrs={'class':'form-control', 'placeholder':'Your full name'}),
            'client_email': EmailInput(attrs={'class':'form-control', 'placeholder':'Your email address'}),
            'client_phone_number': TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
            'client_address': TextInput(attrs={'class':'form-control', 'placeholder':'Your physical address'}),
        }