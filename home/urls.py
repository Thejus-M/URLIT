
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('details/',views.UserDataListView.as_view(),name='details'),
    path('login/',views.LoginInterfaceView.as_view(),name='login'),
    path('logout/',views.LogoutInterfaceView.as_view(),name='logout'),
    path('signup/',views.SignupCreateView.as_view(),name='signup'),
    path('shorten-url/',views.ShortURLCreateView.as_view(),name='shorten-url'),
    path('delete/<pk>',views.URLDeleteView.as_view(),name='delete'),
    path("<slug:slug>", views.Redirecting, name="redirect"),
    # path('<pk>',views.ShortURLCreateView.as_view(),name='shorten-url'),
    
]