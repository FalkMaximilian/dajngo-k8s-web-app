from django.contrib import admin
from django.urls import path
from .views import hallo_schatz

urlpatterns = [
    path('', hallo_schatz, name='hallo-schatz'),
]
