from django.shortcuts import render
from django.http import HttpResponse #importing http-response library
# Create your views here.


# Create your views here.

def index(request):
    diction={'msg':'this is my message to u from view'}
    return render(request,'my_app/index.html',context=diction)


def home(request):
    return HttpResponse("<h5>Home</h5> <a href='/index'>Index</a> <a href='/about'>About</a> <a href='/contact'>Contact</a>")




def about(request):
    return HttpResponse("<h5>About</h5> <a href='/index'>Index</a> <a href='/'>Home</a> <a href='/contact'>Contact</a>")

def contact(request):
    return HttpResponse("<h5>Contact</h5> <a href='/index'>Index</a> <a href='/about'>About</a> <a href='/'>Home</a>")