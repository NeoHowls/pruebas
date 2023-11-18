from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Ruta Home
    path('', include('Website.routes.urls'), name="app1-rutas_home"),
    #Rutas de acceso
    path('', include('Website.routes.urls_access'), name="app1-rutas_acceso"),
    #Rutas de gestión de usuarios
    path('', include('Website.routes.urls_users'), name="app1-rutas_usuarios"),
    #Rutas para json
    path('', include('Website.routes.urls_json'), name="app1-rutas_ajax")
]
