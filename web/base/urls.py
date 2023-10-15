from django.contrib import admin
from django.urls import path
from .views import hallo_schatz, login_page

urlpatterns = [
    path('', hallo_schatz, name='hallo-schatz'),
    path('login/', login_page, name='login-page')
]
