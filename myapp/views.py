from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .forms import Signin, Signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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

class SignUpView(FormView):
	form_class = UserCreationForm
	template_name = 'myapp/signup.html'
	success_url = '/thanks/'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password1)
		login(request, user)
		return super(SignUpView, self).form_valid(form)

class HomeTemplate(TemplateView):
	signup_class = Signup

	def get(self,request,*args,**kwargs):
		user = self.signup_class()
		return render(request,self.template_name, {'user': user})