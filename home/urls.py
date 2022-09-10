
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('details/',views.UserDataListView.as_view(),name='details'),
    
]