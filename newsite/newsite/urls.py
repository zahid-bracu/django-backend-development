
from django.contrib import admin
from django.urls import path
from django.conf.urls import include  #need to import


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls'))
]
