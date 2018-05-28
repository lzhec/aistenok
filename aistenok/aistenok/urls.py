from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('landing.urls'))
]
