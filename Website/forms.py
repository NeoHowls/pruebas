from django import forms
from .models import UserMetadata, Inventory
from .validators import *
from django.utils.html import format_html

#FORMULARIOS
#Formulario destinado a extender el que trae Django Admin por defecto para crear usuarios. De esta forma incluyo los campos correspondientes a la metadata de usuarios
class UserMetadataForm(forms.ModelForm):
    class Meta:
        model = UserMetadata
        fields = '__all__'


#Para extender el de inventario
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'


#Iniciar sesión
class LoginForm(forms.Form):
    rutField = forms.CharField(required=True, widget=forms.TextInput(attrs={'name':'rut', 'id':'input-rut', 'placeholder':'RUT', 'autocomplete':'off'}))
    passwordField = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'name':'password', 'id':'input-password', 'placeholder':'Contraseña'}))

#Crear cuenta
class SignupForm(forms.Form):
    rutField = forms.CharField(required=True, widget=forms.TextInput(attrs={'name':'rut', 'id':'input-rut', 'placeholder':'RUT'}))
    nameField = forms.CharField(required=True, widget=forms.TextInput(attrs={'name':'name', 'id':'input-name', 'placeholder':'Nombre'}))
    lastNameField = forms.CharField(required=True, widget=forms.TextInput(attrs={'name':'lastname', 'id':'input-lastname', 'placeholder':'Apellido'}))
    emailField = forms.EmailField(required=True, widget=forms.TextInput(attrs={'name':'email', 'id':'input-email', 'placeholder':'Correo electrónico'}))
    passwordField = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'name':'password', 'id':'input-password', 'placeholder':'Contraseña'}))
    confirmPasswordField = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'name':'confirm_password', 'id':'input-confirm_password', 'placeholder':'Confirmar contraseña'}))
    numberField = forms.CharField(required=True, widget=forms.TextInput(attrs={'name':'number', 'id':'input-number', 'placeholder':'Teléfono (Opcional) (Omitir el +569)'}))