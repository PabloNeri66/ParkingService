from django.contrib import admin
from parking.models import ParkingRecord, ParkingSpot

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied',]
    search_fields = ['spot_number']
    list_filter = ['is_occupied']

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time',]
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number'] #tabela de Ligacao
    
    #Para evitar duplicacao pelo display do create register de uma  vaga de estacionamento ja ocupada.
    #O Django Admin não oferece uma maneira direta e elegante de diferenciar entre a view de criação e a de edição dentro do formfield_for_foreignkey.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)