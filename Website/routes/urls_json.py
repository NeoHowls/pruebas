from django.urls import path

#Módulos de vistas
from Website.views.json import *

urlpatterns = [
    #RUTAS PARA LISTAS JSON
    #Lista de regiones
    path('regions/', get_regions, name="website-ruta_get-regions"),
    path('comunes/<int:regions_id>', get_comunes, name="website-ruta_get-comunes"),
    path('stations/<int:comunes_id>', get_fireStations, name="website-ruta_get-stations"),
    path('profiles/', get_profiles, name="website-ruta_get-profiles"),
]