from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email Address'}),max_length=100, required=True)
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Password'}),max_length=100, required=True)
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Re-Password'}),max_length=100, required=True)


