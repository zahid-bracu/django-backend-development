 
from django.contrib import admin
from django.urls import path
from django.conf.urls import include #need to add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo_app/', include('demo_app.urls'))

]
