from django.contrib import admin
from django.urls import path
from . import views

# Inbuild views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"), # Name used for url linking 
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='namma_pandit_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='namma_pandit_app/logout.html'), name='logout'),
    path('profile/', views.profile, name="profile")
       
]
