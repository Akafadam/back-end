from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Signin, Signup
from django.contrib.auth import login, authenticate

class SigninTemplate(TemplateView):
	initial = {'key': 'value'} 
	signin_class = Signin

	def get(self, request, *args, **kwargs):
		signin = self.signin_class(initial=self.initial)
		return render(request,self.template_name, {'signin': signin,})

	def post(self, request, *args, **kwargs):
		signin = self.signin_class(request.POST)
		if signin.is_valid:
			pass
		
		return render(request,self.template_name, {'signin': signin,})

class SignupTemplate(TemplateView):
	initial = {'key': 'value'}
	signup_class = Signup

	def get(self,request, *args, **kwargs):
		registration = self.signup_class(initial=self.initial)
		return render(request,self.template_name, {'registration': registration})

	def post(self,request, *args, **kwargs):
		registration = self.signup_class(request.POST)
		if registration.is_valid:
			registration.save()
			username = registration.cleaned_data('username')
			password = registration.cleaned_data('password1')
			user = authenticate(username=username, password=password)
			login(request, user)

		return render(request,self.template_name, {'registration': registration})