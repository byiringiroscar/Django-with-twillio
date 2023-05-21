from django.contrib import admin
from django.urls import path, include

from . import views

name = 'accounts'

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('otp', views.otp, name='otp')
]
