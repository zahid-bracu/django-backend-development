from django.shortcuts import render
from django.http import HttpResponse #importing http-response library
# Create your views here.

def index(request):
    return HttpResponse("<h1>This is index page </h1>")

def home(request):
    return HttpResponse("<h2>This is home page </h2>")