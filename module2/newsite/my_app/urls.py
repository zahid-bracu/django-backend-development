from django.conf.urls import url
from django.urls import path
from my_app import views


urlpatterns = [
    #describe url pattern
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]