from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('home/', views.HomeTemplate.as_view(),name='home'),
	path('login/', views.SigninTemplate.as_view(),name='login'),
	path('signup/', views.SignUpView.as_view(),name='signin'),
]