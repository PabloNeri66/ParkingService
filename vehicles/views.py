from django.shortcuts import render
from rest_framework import viewsets
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer
# Create your views here.

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer