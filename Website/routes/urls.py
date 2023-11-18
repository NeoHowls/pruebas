from django.urls import path, include

#Módulos de vistas
from Website.views.home import *
from Website.views.access import *

urlpatterns = [
    #RUTA PRINCIPAL
    #Inicio
    path('', home, name="website-ruta_home"),
]