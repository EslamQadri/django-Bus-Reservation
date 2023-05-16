from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bus.serializers import BusSerializer, TripSerializer
from bus.models import Bus, Trip


class CreateTripView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class CreateBusViwe(ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class TripRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
