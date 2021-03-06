"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views #import all view from first_app




urlpatterns = [
    path('admin/', admin.site.urls),

    # url pattern , view , view-name pass
    path('index/', views.index, name="index"), #connecting the index view
    path('home/', views.home, name="home"), #connecting the home view
    path('about/', views.about, name="about"), #connecting the about view
    path('contact/', views.contact, name="contact"), #connecting the home view
    path('', views.home, name="home") #connecting the default view
]
