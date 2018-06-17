from django.shortcuts import render
from django.views.generic import TemplateView

class NameTemplate(TemplateView):
	template_name = 'myapp/signin.html'

	def get(self,request):
		return render(request,self.template_name)