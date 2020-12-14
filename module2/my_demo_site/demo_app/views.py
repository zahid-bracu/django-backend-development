from django.shortcuts import render
from django.http import HttpResponse #importing http-response library
# Create your views here.

#now creating a view function
def home(request):
    return HttpResponse("<h3>This is Home</h3>  <a href='index/'>Index<a/>  <a href='about/'>About</a> <a href='contact/'>Contact</a>  ")




def index(request):
    return HttpResponse("<h4>This is index page</h4> <a href='/home/'>Home<a/>  <a href='/about/'>About</a> <a href='/contact/'>Contact</a>  ")

#2nd page view



def about(request):
    return HttpResponse("<h3>This is About page</h3> <a href='/home/'>Home<a/>  <a href='/index/'>Index</a> <a href='/contact/'>Contact</a>  ")

def contact(request):
    return HttpResponse("<h3>This is contact</h3> <a href='/home/'>Home<a/>  <a href='/about/'>About</a> <a href='/index/'>Index</a>  ")

