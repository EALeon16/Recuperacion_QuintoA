from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.alquiler, name = 'alquiler'),
    path('getAll/', views.allAlquileres),
    
]