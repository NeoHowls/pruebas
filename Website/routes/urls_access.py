from django.urls import path

#Módulos de vistas
from Website.views.access import *

#-----RUTAS DE ACCESO-----
urlpatterns = [
    #Iniciar sesión
    path('login', loginView, name="website-ruta_login"),
    #Login para decorator
    path('accounts/login/', loginView, name="website-ruta_redirect_login"),
    #Crear cuenta
    path('signup', signupView, name="website-ruta_signup"),
    #Cuenta creada
    path('signup/success', signupSuccessView, name="website-ruta_signup_success"),
    #Cerrar sesión
    path('logout', logoutView, name="website-ruta_logout"),
]