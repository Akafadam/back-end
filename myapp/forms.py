from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signin(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class Signup(UserCreationForm):
	username = forms.CharField(required=False,help_text='',widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	email = forms.EmailField(required=False,help_text='',widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
	password = forms.CharField(required=False,help_text='',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	check_password = forms.CharField(required=False,help_text='',widget=forms.PasswordInput(attrs={'placeholder': 'Password(Comfirm)'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'check_password', )