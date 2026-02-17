from django import forms
from product.models import *


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput) 


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'payment_method', 'address', 'contact', 'email']

