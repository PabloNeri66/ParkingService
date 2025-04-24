from django.urls import path, include
from  rest_framework.routers import DefaultRouter

from vehicles.views import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register('vehicles/', VehicleViewSet)
router.register('vehicles/type', VehicleTypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
