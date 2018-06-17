from django.shortcuts import render
from django.views.generic import TemplateView

class SigninTemplate(TemplateView):
	template_name = 'myapp/signin.html'

	def get(self,request):
		return render(request,self.template_name)

class SignupTemplate(TemplateView):
	template_name = 'myapp/signup.html'

	def get(self,request):
		return render(request,self.template_name)