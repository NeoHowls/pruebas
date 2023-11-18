from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from ..models import Region, Comune, FireStation, Profile

#Obtener regiones
def get_regions(request):
    regions = list(Region.objects.values())

    if (len(regions) > 0):
        data = {'message':"Success", 'regions': regions}
    else:
        data = {'message':"Not Found"}

    return JsonResponse(data)

#Obtener comunas
def get_comunes(request, regions_id):
    comunes = list(Comune.objects.filter(regions_id=regions_id).values())

    if (len(comunes) > 0):
        data = {'message':"Success", 'comunes': comunes}
    else:
        data = {'message':"Not Found"}

    return JsonResponse(data)

#Obtener estaciones de bomberos
def get_fireStations(request, comunes_id):
    stations = list(FireStation.objects.filter(comunes_id=comunes_id).values())

    if (len(stations) > 0):
        data = {'message':"Success", 'stations': stations}
    else:
        data = {'message':"Not Found"}

    return JsonResponse(data)

#Obtener perfiles de usuario (exceptuando el de administrador)
def get_profiles(request):
    profiles = list(Profile.objects.exclude(id=6).values())

    if (len(profiles) > 0):
        data = {'message':"Success", 'profiles': profiles}
    else:
        data = {'message':"Not Found"}

    return JsonResponse(data)