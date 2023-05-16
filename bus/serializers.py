from rest_framework.serializers import ModelSerializer
from bus.models import Bus, Trip


class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"
