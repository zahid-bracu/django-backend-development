from django.conf.urls import url
from django.urls import path
from demo_app import views

urlpatterns = [
     

    # url pattern , view , view-name pass
    path('index/', views.index, name="index"), #connecting the index view
    path('home/', views.home, name="home"), #connecting the home view
    path('about/', views.about, name="about"), #connecting the about view
    path('contact/', views.contact, name="contact"), #connecting the home view
    path('', views.home, name="home") #connecting the default view
]