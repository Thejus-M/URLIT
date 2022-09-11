from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm  
from .models import UserData,URL


class HomeView(TemplateView):
    template_name = "home/home.html"


class UserDataListView(LoginRequiredMixin,ListView):
    model = UserData
    login_url='login'
    context_object_name = 'urls'
    template_name = "home/home.html"


class LoginInterfaceView(LoginView):
    template_name='home/login.html'
    

class LogoutInterfaceView(LogoutView):
    template_name='home/home.html'



class SignupCreateView(CreateView):
    form_class=UserCreationForm
    success_url='/details'
    template_name = "home/login.html"


class ShortURLCreateView(CreateView):
    model=URL
    # fields=['url_link','short_code']
    fields='__all__'
    success_url='/details'
    template_name = "home/login.html"