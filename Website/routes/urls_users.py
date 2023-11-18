from django.urls import path

#Módulos de vistas
from Website.views.users import *

#-----RUTAS DE GESTIÓN DE USUARIOS-----
urlpatterns = [
    #Lista de usuarios
    path('management_users/list_users', listUsersView, name="website-ruta_list_users"),
    #Agregar usuario
    path('management_users/add_user', addUserView, name="website-ruta_add_user"),
    #Modificar usuario
    path('management_users/update_user/<int:user_id>', updateUserView, name="website-ruta_update_user"),
    #Eliminar usuario
    path('management_users/delete_user/<int:user_id>', deleteUserView, name="website-ruta_delete_user"),
    #Lista de usuarios por aprobar
    path('management_users/approve_users', listApproveUsersView, name="website-ruta_approve_users"),
    #Confirmar aprobar usuario
    path('management_users/approve_users/confirm/<int:user_id>', approveUserConfirmView, name="website-ruta_approve_users_confirm"),
    #Confirmar rechazar usuario
    path('management_users/approve_users/decline/<int:user_id>', approveUserDeclineView, name="website-ruta_approve_users_decline"),
    #Función - Activar usuario
    path('active_user_function/<int:user_id>', activeUser, name="website-ruta_active_user_function"),
    #Función - Eliminar usuario
    path('delete_user_function/<int:user_id>', deleteUser, name="website-ruta_delete_user_function"),
]