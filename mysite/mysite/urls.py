"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import index, signup, login, contact, about, edit, save_message, save_user_info, display_users, display_messages



urlpatterns = [
    path('save-user-info/', save_user_info, name='save_user_info'),
    path('save-message/', save_message, name='save_message'),
    path("messages/", display_messages, name="messages"),
    path('users/', display_users, name='users'),
    path('', index, name='index'),
    path('signup/', signup, name="signup"), 
    path('edit/', edit, name="edit"), 
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    
]
