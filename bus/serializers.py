from rest_framework.serializers import ModelSerializer
from bus.models import Bus, Trip


class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        feilds = "__all__"


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        feilds = "__all__"
