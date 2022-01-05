from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new


urlpatterns = [
path('admin/', admin.site.urls),
path('users/', include('users.urls')),
path('users/', include('django.contrib.auth.urls')),
path('', TemplateView.as_view(template_name='home.html'),
name='home'),
path('articles/', include('articles.urls')),
]