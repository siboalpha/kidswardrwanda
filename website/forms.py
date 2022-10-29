from dataclasses import field
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, EmailInput
from .models import Order, Contact


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


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = {'first_name', 'last_name', 'email', 'phone_number','message'}

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Your last name'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Your email address'}),
            'phone_number': TextInput(attrs={'class':'form-control', 'placeholder':'Your phone number'}),
            'message': Textarea(attrs={'class':'form-control', 'placeholder':'Type your message here', 'cols':'3'}),
        }