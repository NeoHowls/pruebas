from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .validators import *
import os


#Perfiles de usuario
class Profile(models.Model):
    #Nombre del rol
    name = models.CharField(verbose_name="Nombre", max_length=100, unique=True, help_text="Ingrese el nombre del rol")
    #Descripción del rol (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción del rol")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "profiles"
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuario"



#Regiones de Chile
class Region(models.Model):
    #Nombre de la región
    name = models.CharField(verbose_name="Nombre", unique=True, max_length=100, help_text="Ingrese el nombre de la región")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "regions"
        verbose_name = "Región de Chile"
        verbose_name_plural = "Regiones de Chile"



#Comunas de Chile
class Comune(models.Model):
    #Nombre de la comuna
    name = models.CharField(verbose_name="Nombre" ,max_length=100, help_text="Ingrese el nombre de la comuna")
    #Región correspondiente
    regions = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región", help_text="Seleccione la región correspondiente")

    def __str__(self):
        return self.name
    
    def get_region_display(self):
        return self.regions.name
    
    class Meta:
        db_table = "comunes"
        verbose_name = "Comuna de Chile"
        verbose_name_plural = "Comunas de Chile"



#Estaciones de bomberos
class FireStation(models.Model):
    #Nombre de la estación
    name = models.CharField(verbose_name="Nombre", max_length=100, unique=True, help_text="Ingrese el nombre de la estación")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción de la estación")
    #Dirección
    address = models.CharField(verbose_name="Dirección", max_length=100, help_text="Ingrese la dirección (calle y número) de la estación")
    #Comuna correspondiente
    comunes = models.ForeignKey(Comune, on_delete=models.DO_NOTHING, verbose_name="Comuna", help_text="Seleccione la comuna correspondiente")
    #Fecha de creación
    create_date = models.DateTimeField(verbose_name="Fecha de creación", default=timezone.now, editable=False)

    def __str__(self):
        return self.name
    
    def get_comune_display(self):
        return self.comunes.name

    class Meta:
        db_table = "fire_stations"
        verbose_name = "Estación de bomberos"
        verbose_name_plural = "Estaciones de bomberos"


# Metadata de usuarios
class UserMetadata(models.Model):
    #Usuario correspondiente
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="ID Usuario")
    #Perfil de usuario
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, verbose_name="Rol de usuario", help_text="Ingrese el rol del usuario")
    #Teléfono
    number = models.CharField(verbose_name="Teléfono", help_text="Ingresar número de teléfono", max_length=15)
    #Estación de bomberos perteneciente
    fire_stations = models.ForeignKey(FireStation, on_delete=models.DO_NOTHING, verbose_name="Estación de bomberos", help_text="Seleccione la estación correspondiente")

    class Meta:
        db_table = "user_metadata"
        verbose_name = "Metadata de usuario"
        verbose_name_plural = "Metadatos de usuarios"



#Tipos de estado
#class TypeStatus(models.Model):
#    #Nombre
#    name = models.CharField(verbose_name="Nombre", max_length=100, unique=True, help_text="Ingrese el tipo de estado")
#    #Descripción (opcional)
#    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción del tipo de estado")
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        db_table = "type_status"
#        verbose_name = "Tipo de estado"
#        verbose_name_plural = "Tipos de estado"



#Estados
class Status(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=100, help_text="Ingrese el nombre del estado")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción del estado")
    #Tipo de estado correspondiente
    #type_status = models.ForeignKey(TypeStatus, on_delete=models.CASCADE, verbose_name="Tipo de estado", help_text="Seleccione el tipo de estado")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "status"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"



#Tipos de carros bomba
class TypeFireTruck(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=50, help_text="Ingrese el nombre del tipo de vehículo")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción del tipo de vehículo")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type_fire_trucks"
        verbose_name = "Tipo de vehículo bomberil"
        verbose_name_plural = "Tipos de vehículos bomberiles"



#Unidades (Carros bomba)
class FireTruck(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=100, help_text="Ingrese un nombre de fantasía para el vehículo")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingrese una descripción para el vehículo")
    #Patente del vehículo
    plate = models.CharField(verbose_name="Patente", max_length=15, unique=True, help_text="Ingrese el número de patente del vehículo")
    #Modelo (opcional)
    model = models.CharField(verbose_name="Modelo", max_length=50, blank=True, null=True, help_text="(Opcional) Ingrese el modelo del vehículo")
    #Número de chasis (opcional)
    vin = models.CharField(verbose_name="Chasis", max_length=50, unique=True, blank=True, null=True, help_text="(Opcional) Ingrese el número de chasis del vehículo")
    #Año (opcional)
    year = models.IntegerField(verbose_name="Año", blank=True, null=True, help_text="(Opcional) Ingrese el año de fabricación del vehículo")
    #Tipo de unidad
    type_fire_trucks = models.ForeignKey(TypeFireTruck, on_delete=models.DO_NOTHING, verbose_name="Tipo de vehículo", help_text="Seleccionar tipo de vehículo")
    #Estación correspondiente
    fire_stations = models.ForeignKey(FireStation, on_delete=models.DO_NOTHING, verbose_name="Estación de bomberos", help_text="Seleccionar bomba/estación")
    #Estado
    #status = models.ForeignKey(Status, models.DO_NOTHING, null=True)
    #Imagen (opcional)
    image = models.ImageField(verbose_name="Imagen", upload_to="firetrucks", default="default.png", unique=True, blank=True, null=True, help_text="(Opcional) Subir imagen del vehículo")
    #Fecha de creación
    create_date = models.DateTimeField(verbose_name="Fecha de creación", auto_now=True, editable=False)

    def __str__(self):
        return self.name
    
    def get_type_fire_truck_display(self):
        return self.type_fire_trucks.name
    
    def delete(self, *args, **kwargs):
        # Borrar la imagen asociada
        if self.image:
            # Obtiene la ruta completa del archivo de imagen
            image_path = self.image.path
            print(f"Intentando eliminar imagen: {image_path}")

            # Borra el archivo de imagen
            if os.path.isfile(image_path):
                if (self.image.name == self._meta.get_field('image').get_default()):
                    pass
                else:
                    os.remove(image_path)
                    print(f"Imagen eliminada: {image_path}")

        super(FireTruck, self).delete(*args, **kwargs)

    class Meta:
        db_table = "fire_trucks"
        verbose_name = "Vehículo Bomberil"
        verbose_name_plural = "Vehículos Bomberiles"



#Compartimentos de las unidades (gabetas)
class Compartment(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=100, help_text="Ingrese el nombre de la gaveta/compartimento")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingresar descripción para la gaveta/compartimento")
    #Cantidad estándar de insumos
    quantity = models.IntegerField(verbose_name="Cantidad", blank=True, null=True, help_text="(Opcional) Aquí se establece la cantidad esperada de insumos del compartimento. Puede definirse después")
    #Unidad correspondiente
    fire_trucks = models.ForeignKey(FireTruck, on_delete=models.CASCADE, verbose_name="Vehículo", help_text="Seleccionar vehículo bomberil correspondiente")

    def __str__(self):
        return self.name
    
    def get_fire_truck_display(self):
        return self.fire_trucks.name

    class Meta:
        db_table = "compartments"
        verbose_name = "Gaveta de almacenamiento"
        verbose_name_plural = "Gavetas de almacenamiento"



#Operaciones (llamados de emergencia)
class FireOperation(models.Model):
    #Usuario que realizó la operación
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="ID de usuario", editable=False)
    #Unidad
    fire_trucks = models.ForeignKey(FireTruck, on_delete=models.DO_NOTHING, verbose_name="Vehículo", null=False, editable=False)
    #Inicio
    start_at = models.DateTimeField(verbose_name="Hora de inicio", null=False, editable=False)
    #Término
    end_at = models.DateTimeField(verbose_name="Hora de término", null=False, editable=False)

    class Meta:
        db_table = "fire_operation"
        verbose_name = "Operación"
        verbose_name_plural = "Operaciones"



#Categorías (de inventario)
class Category(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=100, unique=True, help_text="Ingrese el nombre de la categoría")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingresar descripción de la categoría")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name = "Categoría de insumo"
        verbose_name_plural = "Categorías de insumos"


#Sub categorías (de inventario)
#class SubCategory(models.Model):
#    #Nombre
#    name = models.CharField(verbose_name="Nombre", max_length=100, unique=True, help_text="Ingresar nombre general de insumo (Ej: Casco, hacha, extintor). La subcategoría está destinada a agrupar insumos que, en esencia, son lo mismo (puede variar el fabricante, modelo o sólo cualidades estéticas)")
#    #Descripción (opcional)
#    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingresar descripción de la sub categoría")
#    #Categoría
#    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría", help_text="Seleccionar categoría")
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        db_table = "sub_categories"
#        verbose_name = "Sub categoría de insumo"
#        verbose_name_plural = "Sub categorías de insumos"


#Programas de mantenimiento
class MaintenanceProgram(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100, help_text="Ingrese un título para facilitar la identificación del programa")
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, editable=False)
    day = models.IntegerField(verbose_name="Día del mes", help_text="Establecer día del mes para efectuar la mantención. Seleccione entre 1 y 30", validators=[validate_month_day])
    frequency = models.IntegerField(verbose_name="Mantenimiento cada (días)", default=30, help_text="Indicar la frecuencia de mantención (días)")
    notification = models.IntegerField(verbose_name="Notificación anticipada (días)", default=1, help_text="Indicar con cuantos días de anticipación notificar")

    def __str__(self):
        return self.name
    
    def get_user_display(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"

    class Meta:
        db_table = "maintenance_program"
        verbose_name = "Programa de mantenimiento"
        verbose_name_plural = "Programas de mantenimiento"



#Inventario - Tabla principal
class Inventory(models.Model):
    #Código de barras
    sku = models.IntegerField(verbose_name="Código de barras", unique=True, blank=True, null=True)
    #Categoría
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categoría", help_text="Seleccionar categoría")
    #Tipo de insumo
    #sub_categories_id = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, verbose_name="Sub categoría", help_text="Seleccionar sub categoría")
    #Ubicación (gabeta)
    compartments = models.ForeignKey(FireTruck, on_delete=models.CASCADE, verbose_name="Gabeta/compartimento", help_text="Seleccionar en qué gabeta está ubicado")
    #Estado
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name="Estado", help_text="Definir estado del insumo")
    #Fecha de expiración (opcional)
    expire_at = models.DateField(verbose_name="Fecha de Vencimiento", blank=True, null=True, help_text="(Opcional) Indicar fecha de expiración si corresponde")
    #Elegir días de anticipación para notificar la caducidad. Por defecto son 30 días (opcional)
    expire_notification = models.IntegerField(verbose_name="Notificación de caducidad", blank=True, null=True, help_text="(Opcional) Indicar con cuántos días de anticipación se desea recibir un aviso de caducidad próxima")
    #Mantenimiento - Horas de uso para mantenimiento (opcional)
    maintenance_hour = models.IntegerField(verbose_name="Horas de uso para mantenimiento", blank=True, null=True, help_text="(Opcional) Indicar cada cuántas horas de uso se debe hacer mantenimiento")
    #Horas de uso (opcional)
    usage_hours = models.IntegerField(verbose_name="Horas de uso", default=0, help_text="(Opcional) Horas de uso reseteables")
    #Total horas de uso (opcional)
    total_usage_hours = models.IntegerField(verbose_name="Horas de uso totales", default=0, help_text="(Opcional) Horas de uso totales. Por defecto es cero")
    #Insumo contenedor (opcional)
    container = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Insumo contenedor", blank=True, null=True, help_text="(Opcional) Si el insumo está contenido dentro de otro insumo, indicarlo aquí")
    #Programa de mantenimiento (opcional)
    maintenance_programs = models.ForeignKey(MaintenanceProgram, on_delete=models.DO_NOTHING, verbose_name="Programa de mantenimiento" ,blank=True, null=True, help_text="(Opcional) Indicar programa de mantención si corresponde")
    #Fecha de última mantención
    last_maintenance = models.DateField(verbose_name="Última mantención", blank=True, null=True)
    #Fecha de ingreso al sistema
    create_date = models.DateTimeField(verbose_name="Fecha de creación", default=timezone.now, editable=False)

    class Meta:
        db_table = "inventory"
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"

    def __str__(self):
        return self.inventorymetadata.name

    def get_category_display(self):
        return self.categories.name
    
    def get_compartment_display(self):
        return self.compartments.name
    
    def get_status_display(self):
        return self.status.name


#Inventario - Metadata
class InventoryMetadata(models.Model):
    #Nombre
    name = models.CharField(verbose_name="Nombre", max_length=100, help_text="Ingrese el nombre de fantasía del insumo. Puede ser su nombre comercial")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingresar descripción del insumo")
    #Precio (opcional)
    price = models.IntegerField(verbose_name="Precio", blank=True, null=True, help_text="(Opcional) Ingresar valor comercial del insumo")
    #Marca (opcional)
    brand = models.CharField(verbose_name="Marca", max_length=50, blank=True, null=True, help_text="(Opcional) Ingresar marca del insumo")
    #Modelo (opcional)
    model = models.CharField(verbose_name="Modelo", max_length=50, blank=True, null=True, help_text="(Opcional) Ingresar modelo del insumo")
    #Insumo correspondiente
    Inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, verbose_name="Insumo", help_text="Seleccionar insumo correspondiente")
    #Imagen (opcional)
    image = models.ImageField(verbose_name="Imagen", upload_to="inventory", default="default.png", unique=True, blank=True, null=True, help_text="(Opcional) Subir imagen del insumo")
    #Fecha de ingreso al sistema
    create_date = models.DateTimeField(verbose_name="Fecha de creación", default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "inventory_metadata"
        verbose_name = "Insumo - Metadata"
        verbose_name_plural = "Insumos - Metadata"


#Prestaciones de inventario
class LendingItems(models.Model):
    #Insumo
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name="Insumo", help_text="Insumo prestado")
    #A quién se le prestó
    entity = models.CharField(verbose_name="Persona / Entidad", max_length=100, help_text="A quién se le prestó el insumo")
    #Descripción (opcional)
    description = models.TextField(verbose_name="Descripción", blank=True, null=True, help_text="(Opcional) Ingresar descripción del insumo")
    #Fecha de creación
    create_date = models.DateTimeField(verbose_name="Fecha" ,auto_now=True, editable=False)

    class Meta:
        db_table = "lending_items"
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos de insumos"