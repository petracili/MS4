from django.contrib import admin
from django.urls import path
from .views import all_plants

urlpatterns = [
    path('plants', all_plants, name='plants'),
]