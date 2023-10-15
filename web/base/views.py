from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def hallo_schatz(request):
    return render(request, 'templates/login_page.html')