from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def hallo_schatz(request):
    return HttpResponse('<div style="width:100%;height:100%;text-align:center;justify-content:center;padding-top:auto;padding-bottom:auto;"><h1>Hallo Schatz! Liebe Grüße aus Spandau :*</h1></div>')