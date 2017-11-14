from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user_name']

class UpdateForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput)
    old_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['old_password','new_password']
