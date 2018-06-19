from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signin(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
