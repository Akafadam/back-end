from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Signin

class SigninTemplate(TemplateView):
	template_name = 'myapp/signin.html'
	initial = {'key': 'value'} 
	email_class = Signin.get_email
	password_class = Signin.get_password

	def get(self, request, *args, **kwargs):
		email = self.email_class(initial=self.initial)
		password = self.password_class(initial=self.initial)
		return render(request,self.template_name, {'email': email, 'password': password,})

class SignupTemplate(TemplateView):
	template_name = 'myapp/signup.html'

	def get(self,request):
		return render(request,self.template_name)