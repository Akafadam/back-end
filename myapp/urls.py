from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = {
	  path('login/', views.SigninTemplate.as_view(template_name='myapp/signin.html')),
	  path('signup/', views.SignupTemplate.as_view(template_name='myapp/signup.html')),
}