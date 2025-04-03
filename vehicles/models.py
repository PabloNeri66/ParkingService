from django.db import models
from costumers.models import Costumer


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nome do Veículo',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipo de veículo'
        verbose_name_plural = 'Tipos de veículos'
    

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='Vehicles',
        verbose_name='Tipo de Veículo',
    )
    #License Plate é Requisito Funcional.
    license_plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa',
    )
    #Má pratica. Fazer um objeto Brand...
    brand = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name='Marca',
        )
    model = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name='Modelo',
        )
    color = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name='Cor',
        )
    owner = models.ForeignKey(
        Costumer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Proprietário',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em',
        )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em',
        )

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate # Stringar na interface.