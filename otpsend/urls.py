from django.contrib import admin
from django.urls import path, include
from . import views

name = 'otpsend'

urlpatterns = [
    path('', views.check, name='check'),
    path('plate', views.capture_plate, name='capture_plate')
]