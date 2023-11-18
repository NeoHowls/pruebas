from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Website.models import *
from .forms import *

#EXTENDER FORMULARIO PARA LAS 2 TABLAS DE USUARIO
#Clase personalizada para modelo UserMetadata
class UserMetadataInline(admin.StackedInline):
    model = UserMetadata
    form = UserMetadataForm

#Cambiar nombre de fantasía del campo 'username'
User._meta.get_field('username').verbose_name = 'RUT (Nombre de usuario)'
User._meta.get_field('username').help_text = 'Ingrese el RUT (Rol Único Tributario) del usuario con puntos y guión'

#Clase personalizada para modelo User
class CustomUserAdmin(UserAdmin):
    inlines = [UserMetadataInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_profiles_id', 'is_active', 'is_staff', 'date_joined')

    def get_profiles_id(self, obj):
        # Accede al campo 'profiles_id' desde UserMetadata a través de la relación 'usermetadata'
        return obj.usermetadata.profiles.name
    
    #Nombre personalizado para las columnas relacionadas
    get_profiles_id.short_description = 'Rol'


#EXTENDER FORMULARIO PARA LAS 2 TABLAS DE INVENTARIO
#Clase personalizada para modelo Inventory
class InventoryMetadataInline(admin.StackedInline):
    model = InventoryMetadata
    form = InventoryForm

#Clase para InventoryMetadata
class InventoryAdmin(admin.ModelAdmin):
    inlines = [InventoryMetadataInline]
    list_display = ('id', 'sku', 'get_name', 'get_description', 'get_price','get_category', 'get_compartment', 'expire_at', 'total_usage_hours', 'last_maintenance', 'maintenance_programs_id', 'get_status')
    exclude = ['usage_hours']

    def get_name(self, obj):
        return obj.inventorymetadata.name
    
    def get_description(self, obj):
        return obj.inventorymetadata.description
    
    def get_price(self, obj):
        return obj.inventorymetadata.price
    
    def get_category(self, obj):
        return format_html(f"<a href='/admin/Website/category/{obj.categories_id}/change/'>{obj.get_category_display()}</a>")

    def get_compartment(self, obj):
        return format_html(f"<a href='/admin/Website/compartment/{obj.compartments_id}/change/'>{obj.get_compartment_display()}</a>")
    
    def get_status(self, obj):
        return format_html(f"<a href='/admin/Website/status/{obj.status_id}/change/'>{obj.get_status_display()}</a>")
    
    get_name.short_description = 'Nombre'
    get_description.short_description = "Descripción"
    get_price.short_description = 'Precio'
    get_category.short_description="Categoría"
    get_compartment.short_description="Gaveta"


#MODELOS
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class ComuneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_region')
    search_fields = ('id', 'name')

    def get_region(self, obj):
        return format_html(f"<a href='/admin/Website/region/{obj.regions_id}/change/'>{obj.get_region_display()}</a>")
    get_region.short_description="Región"
    

class FireStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'get_comune')
    search_fields = ('id', 'name')

    def get_comune(self, obj):
        return format_html(f"<a href='/admin/Website/comune/{obj.comunes_id}/change/'>{obj.get_comune_display()}</a>")
    get_comune.short_description="Comuna"

#class TypeStatusAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'description')
#    search_fields = ('id', 'name')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name')

class TypeFireTruckAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name')

class FireTruckAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'plate', 'model', 'year', 'get_type_fire_truck', 'create_date')
    search_fields = ('id', 'name')

    def get_type_fire_truck(self, obj):
        return format_html(f"<a href='/admin/Website/typefiretruck/{obj.type_fire_trucks_id}/change/'>{obj.get_type_fire_truck_display()}</a>")
    get_type_fire_truck.short_description="Tipo de vehículo"

class CompartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'quantity', 'get_fire_truck')
    search_fields = ('id', 'name')

    def get_fire_truck(self, obj):
        return format_html(f"<a href='/admin/Website/firetruck/{obj.fire_trucks_id}/change/'>{obj.get_fire_truck_display()}</a>")
    get_fire_truck.short_description="Vehículo"

class FireOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'start_at', 'end_at')
    search_fields = ('id', 'user_id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name')

#class SubCategoryAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'description', 'categories_id')
#    search_fields = ('id', 'name')

class MaintenanceProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'day', 'frequency', 'notification', 'get_user')
    search_fields = ('id', 'name')
    exclude = ['user_id']

    def save_model(self, request, obj, form, change):
        # Asignar el usuario actual antes de guardar el objeto
        if not change:  # Solo al crear un nuevo objeto, no cuando se actualiza
            obj.user = request.user
        obj.save()

    def get_user(self, obj):
        return format_html(f"<a href='/admin/Website/user/{obj.user_id}/change/'>{obj.get_user_display()}</a>")
    get_user.short_description="Creado por"

class LendingItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_id_inventory', 'get_inventory', 'entity', 'create_date')
    search_fields = ('id', 'get_inventory', 'entity')

    def get_id_inventory(self, obj):
        return obj.inventory.id
    def get_inventory(self, obj):
        return obj.inventory.inventorymetadata.name
    get_id_inventory.short_description="ID del Insumo"
    get_inventory.short_description="Insumo"

#class NameAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name')
#    search_fields = ('id', 'name')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comune, ComuneAdmin)
admin.site.register(FireStation, FireStationAdmin)
#admin.site.register(TypeStatus, TypeStatusAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(TypeFireTruck, TypeFireTruckAdmin)
admin.site.register(FireTruck, FireTruckAdmin)
admin.site.register(Compartment, CompartmentAdmin)
admin.site.register(FireOperation, FireOperationAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(MaintenanceProgram, MaintenanceProgramAdmin)
admin.site.register(LendingItems, LendingItemsAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.site_header = 'Administrador de Sistema de Inventario'
admin.site.index_title = 'Gestión Principal'
admin.site.site_title = 'Administrador Sistema de Inventario'
