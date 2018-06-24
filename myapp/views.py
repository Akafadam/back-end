from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import Signin, Signup
from django.contrib.auth import login, authenticate

class SigninTemplate(TemplateView):
	signin_class = Signin

	def get(self, request, *args, **kwargs):
		signin = self.signin_class()
		return render(request,self.template_name, {'signin': signin,})

	def post(self, request, *args, **kwargs):
		signin = self.signin_class(request.POST)
		if signin.is_valid:
			pass
		
		return render(request,self.template_name, {'signin': signin,})

class SignupTemplate(TemplateView):
	signup_class = Signup

	def get(self,request, *args, **kwargs):
		registration = self.signup_class()
		return render(request,self.template_name, {'registration': registration})

	def post(self,request, *args, **kwargs):
		registration = self.signup_class(request.POST)
		if registration.is_valid():
			user = registration.save()
			user.refresh_from_db()
			user.save()
			username = registration.cleaned_data.get('username')
			password = registration.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')

		return render(request,self.template_name, {'registration': registration})

class HomeTemplate(TemplateView):
	signup_class = Signup

	def get(self,request,*args,**kwargs):
		user = self.signup_class()
		return render(request,self.template_name, {'user': user})