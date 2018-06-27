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
	signup_class = UserCreationForm
	template_name = 'myapp/signup.html'

	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('https://docs.djangoproject.com')

	return render(request,self.template_name, {'form': form})

class HomeTemplate(TemplateView):
	signup_class = Signup

	def get(self,request,*args,**kwargs):
		user = self.signup_class()
		return render(request,self.template_name, {'user': user})