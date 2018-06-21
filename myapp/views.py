from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Signin, Signup
from django.contrib.auth import login, authenticate

class SigninTemplate(TemplateView):
	template_name = 'myapp/signin.html'
	initial = {'key': 'value'} 
	email_class = Signin

	def get(self, request, *args, **kwargs):
		email = self.email_class(initial=self.initial)
		return render(request,self.template_name, {'email': email,})

class SignupTemplate(TemplateView):
	template_name = 'myapp/signup.html'
	initial = {'key': 'value'}
	email_class = Signup

	def get(self,request, *args, **kwargs):
		registration = self.email_class(initial=self.initial)
		return render(request,self.template_name, {'registration': registration})

	def post(self,request, *args, **kwargs):
		registration = self.email_class(request.POST)
		if registration.is_valid:
			registration.save()
			username = registration.cleaned_data('username')
			password = registration.cleaned_data('password1')
			user = authenticate(username=username, password=password)
			login(request, user)

		return render(request,self.template_name, {'registration': registration})