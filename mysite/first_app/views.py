from django.shortcuts import render
from django.http import HttpResponse #importing http-response library
# Create your views here.

#now creating a view function
def index(request):
    return HttpResponse("<h4>This is index page</h4>")

#2nd page view
def home(request):
    return HttpResponse("<h3>This is Home</h3>")


