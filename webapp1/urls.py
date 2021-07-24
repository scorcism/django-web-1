from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('staff', views.staff, name='staff'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('loginFirst', views.loginFirst, name='loginFirst'),
    path('nostaff', views.nostaff, name='nostaff'),
    path('work', views.work, name='work'),
] 

