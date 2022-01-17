from django.urls import path
from . views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("login",auth_view.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path("logout",auth_view.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path("sign_up",signUp,name='sign_up'),
]