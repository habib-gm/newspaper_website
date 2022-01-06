from django.contrib import admin
from django.urls import path, include
from articles.views import HomeView


urlpatterns = [
path('admin/', admin.site.urls),
path('users/', include('users.urls')),
path('users/', include('django.contrib.auth.urls')),
path('', HomeView.as_view(), name='home'),
path('articles/', include('articles.urls')),
]