from django import forms

class Signin(forms.Form):

	def get_email():
		email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))

	def get_password():
		password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))