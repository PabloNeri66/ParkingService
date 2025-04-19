from rest_framework import serializers
from parking.models import ParkingRecord, ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = '__all__'


class ParkingRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecord
        fields = '__all__'
