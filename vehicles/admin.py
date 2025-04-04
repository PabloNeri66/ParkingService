from django.contrib import admin

# Register your models here.
from vehicles.models import Vehicle, VehicleType


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]
    search_fields = ['name']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color',]
    search_fields = ['license_plate', 'model',] #aqui voce procura através desses campos no search
    list_filter = ['vehicle_type'] #aqui voce filtra através do carro.

    