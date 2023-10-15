from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.

def hallo_schatz(request):
    return redirect('login-page')

def login_page(request):
    return render(request, 'base/login_page.html')