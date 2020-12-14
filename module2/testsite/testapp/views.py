from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    diction={'message':'this is my message'}
    return render(request,'testapp/index.html',context=diction)