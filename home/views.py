from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import UserData


class HomeView(TemplateView):
    template_name = "home/home.html"


class UserDataListView(ListView):
    model = UserData
    context_object_name = 'urls'
    template_name = "home/home.html"

