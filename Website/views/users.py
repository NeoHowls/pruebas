from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import UserMetadata, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from ..forms import *


#Vista - Lista de usuarios registrados
@login_required()
def listUsersView(request):
    users = UserMetadata.objects.filter(user__is_active=True)
    total_users = users.count()

    return render(request, 'Website/management_users/list_users.html', {'active_users':users, 'count_users':total_users})


#Vista - Agregar usuario
@login_required()
def addUserView(request):
    form = SignupForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            #¿El rut existe?
            if (User.objects.filter(username=request.POST['rutField']).exists()):
                messages.add_message(request, messages.WARNING, f"El rut ya está en uso.")
                return HttpResponseRedirect(reverse('website-ruta_add_user'))
            
            #¿Las contraseñas coinciden?
            elif(request.POST['passwordField'] != request.POST['confirmPasswordField']):
                messages.add_message(request, messages.WARNING, f"Las contraseñas no coinciden")
                return HttpResponseRedirect(reverse('website-ruta_add_user'))
            
            #¿Los campos selects tiene valores válidos?
            elif(request.POST['profile'] == 0 or request.POST['station'] == 0):
                messages.add_message(request, messages.WARNING, f"Faltan campos que son obligatorios. Por favor, envíe el formulario completo")
                return HttpResponseRedirect(reverse('website-ruta_add_user'))

            else:
                #Crear registro en la tabla auth_user
                u=User.objects.create_user(username=request.POST['rutField'], password=request.POST['passwordField'], email=request.POST['emailField'], first_name=request.POST['nameField'], last_name=request.POST['lastNameField'], is_active=0)
                #Crear registro en la tabla de metadata
                UserMetadata.objects.create(number=request.POST['numberField'], fire_stations_id=request.POST['station'], profiles_id=request.POST['profile'], user_id=u.id)
                messages.add_message(request, messages.SUCCESS, f"Cuenta creada a la espera de aprobación.")
                return HttpResponseRedirect(reverse('website-ruta_list_users'))
        
        else:
            messages.add_message(request, messages.WARNING, f"No fue posible crear la cuenta. Vuelva a intentarlo.")
            #return HttpResponse(f"{form} - {form.errors} - Perfil = {request.POST['profileField']} - Estación = {request.POST['stationField']}")
            return HttpResponseRedirect(reverse('website-ruta_add_user'))
        
    return render(request, 'Website/management_users/add_user.html', {'form':form})


#Vista - Modificar usuario
@login_required()
def updateUserView(request, user_id):
    #Obtenemos el registro de auth_user para actualizarlo
    user = User.objects.filter(id=user_id)
    #Obtenemos el registro del usuario de la tabla meta
    userMeta = UserMetadata.objects.filter(user_id=user_id).get()
    #Ya que por algún motivo mis funciones js para manejar listas JSON no funcionó en esta vista, obtendré el listado de perfiles de esta manera, ignorando el perfil seleccionado
    profiles = Profile.objects.exclude(id=userMeta.profiles_id)
    #obtenemos el perfil seleccionado para mostrarlo en primera posición
    profile = Profile.objects.filter(id=userMeta.profiles_id).get()
    #Obtenemos el formulario
    form = SignupForm(request.POST or None)

    initial_data = {
        'rutField': userMeta.user.username,  # Asegúrate de que los nombres coincidan con los nombres de tus campos en el formulario
        'nameField': userMeta.user.first_name,
        'lastNameField': userMeta.user.last_name,
        'emailField': userMeta.user.email,
        'numberField': userMeta.number,
    }
    form = SignupForm(initial=initial_data)

    if request.method == 'POST':
        if form.is_valid():
            #¿El rut existe?
            if (User.objects.filter(username=request.POST['rutField']).exists()):
                messages.add_message(request, messages.WARNING, f"El rut ya está en uso.")
                return HttpResponseRedirect(reverse('website-ruta_update_user'))
            
            #¿Las contraseñas coinciden?
            elif(request.POST['passwordField'] != request.POST['confirmPasswordField']):
                messages.add_message(request, messages.WARNING, f"Las contraseñas no coinciden")
                return HttpResponseRedirect(reverse('website-ruta_update_user'))
            
            #¿Los campos selects tiene valores válidos?
            elif(request.POST['profile'] == 0):
                messages.add_message(request, messages.WARNING, f"Faltan campos que son obligatorios. Por favor, envíe el formulario completo")
                return HttpResponseRedirect(reverse('website-ruta_update_user'))

            else:
                #Modificar registro en la tabla auth_user
                user.username = request.POST.get('rutField')
                user.first_name = request.POST.get('nameField')
                user.last_name = request.POST.get('lastNameField')
                user.email = request.POST.get('emailField')
                #Modificar registro en la tabla de metadata
                userMeta.profiles_id = request.POST.get('profile')

                user.save()
                userMeta.save()
                messages.add_message(request, messages.SUCCESS, f"Usuario modificado.")
                return HttpResponseRedirect(reverse('website-ruta_list_users'))
        
        else:
            messages.add_message(request, messages.WARNING, f"No fue posible modificar al usuario. Vuelva a intentarlo.")
            return HttpResponse(f"{form} - {form.errors}")
            return HttpResponseRedirect(reverse('website-ruta_list_users'))


    return render(request, 'Website/management_users/update_user.html', {'userMeta':userMeta, 'form':form, 'profiles':profiles, 'profile':profile})


#Vista - Eliminar usuario
@login_required()
def deleteUserView(request):
    return render(request, 'Website/management_users/delete_user.html', {})


#Vista - Aprobar nuevos usuarios
@login_required()
def listApproveUsersView(request):
    users = UserMetadata.objects.filter(user__is_active=False)
    total_users = users.count()

    # Realiza la lógica para determinar el estado de cada usuario
    for userM in users:
        userM.status = "Aprobado" if userM.user.is_active else "Pendiente de aprobación"
    return render(request, 'Website/management_users/approve_users.html', {'inactive_users':users, 'count_users':total_users})


#Vista - Confirmar aprobación de usuario
@login_required()
def approveUserConfirmView(request, user_id):
    user = User.objects.filter(id=user_id).get()

    return render(request, 'Website/management_users/approve_users_confirm.html', {'user_inactive':user})


#Vista - Rechazar aprobación de usuario
@login_required()
def approveUserDeclineView(request, user_id):
    user = User.objects.filter(id=user_id).get()

    return render(request, 'Website/management_users/approve_users_decline.html', {'user_inactive':user})


@login_required()
#Activar usuario
def activeUser(request, user_id):
    try:
        user = User.objects.filter(id=user_id).get()
        user.is_active=True
        user.save()
        messages.add_message(request, messages.SUCCESS, f'El usuario {user.first_name.title()} {user.last_name.title()} ha sido aprobado con éxito')
        return HttpResponseRedirect(reverse('website-ruta_approve_users'))
    except Exception:
        messages.add_message(request, messages.ERROR, f'No se ha podido aprobar al usuario')
        return HttpResponseRedirect(reverse('website-ruta_approve_users'))


@login_required()
#Eliminar usuario
def deleteUser(request, user_id):
    try:
        user = User.objects.filter(id=user_id).get()
        user.delete()
        messages.add_message(request, messages.SUCCESS, f'El usuario {user.first_name.title()} {user.last_name.title()} ha sido eliminado con éxito')
        return HttpResponseRedirect(reverse('website-ruta_approve_users'))
    except Exception:
        messages.add_message(request, messages.ERROR, f'No se ha podido eliminar al usuario')
        return HttpResponseRedirect(reverse('website-ruta_approve_users'))