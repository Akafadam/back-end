
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('account/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
