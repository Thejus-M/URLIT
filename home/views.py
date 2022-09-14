from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm  
from .models import URL
import string
import random


class HomeView(TemplateView):
    template_name = "home/front_page.html"


class UserDataListView(LoginRequiredMixin,ListView):
    model = URL
    login_url='login'
    context_object_name = 'urls'
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = context['urls'].filter(name=self.request.user)
        return context


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'



def Redirecting(request, slug):
    model = URL
    link = model.objects.filter(short_code=slug).values('url_link')[0]['url_link']
    return redirect(link)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/home.html'



class SignupCreateView(CreateView):
    form_class = UserCreationForm
    success_url = '/details'
    template_name = "home/login.html"



class URLDeleteView(LoginRequiredMixin, DeleteView):
    model = URL
    template_name = "home/confirm_delete.html"
    success_url = '/details'


class ShortURLCreateView(LoginRequiredMixin,CreateView):
    model=URL
    fields=['url_link']
    # fields='__all__'
    success_url='/details'
    template_name = "home/login.html"
    
    
    def form_valid(self, form):
        def random_endpoint():
            random_string = ''
            for _ in range(5):
                # Considering only upper and lowercase letters
                random_integer = random.randint(97, 97 + 26 - 1)
                flip_bit = random.randint(0, 1)
                # Convert to lowercase if the flip bit is on
                random_integer = random_integer - 32 if flip_bit == 1 else random_integer
                # Keep appending random characters using chr(x)
                random_string += (chr(random_integer))
            return random_string
        form.instance.name = self.request.user
        form.instance.short_code = random_endpoint()
        return super().form_valid(form)