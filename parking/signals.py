from django.db.models.signals import post_save
from django.dispatch import receiver

from parking.models import ParkingRecord

@receiver(post_save, sender=ParkingRecord)
def update_parking_spot_status(sender, instance, created, **kwargs):
    parking_spot = instance.parking_spot
    parking_spot.is_occupied = (instance.exit_time is None) #Boolean
    parking_spot.save()
#Tornar a instância do evento(parkingRecord) capaz de mudar o is_occupied da vaga.