from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signin(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class Signup(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254, required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
