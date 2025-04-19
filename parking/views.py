#from django.shortcuts import render
from rest_framework import viewsets
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingSpotSerializer, ParkingRecordSerializer
# Create your views here.


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer