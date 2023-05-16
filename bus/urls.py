from django.urls import path
from bus.views import (
    BusRetrieveUpdateDestroyView,
    CreateBusViwe,
    CreateTripView,
    TripRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("Bus", CreateBusViwe.as_view()),
    path("Bus/<int:pk>/", BusRetrieveUpdateDestroyView.as_view()),
    path("Trip", CreateTripView.as_view()),
    path("Trip/<int:pk>", TripRetrieveUpdateDestroyView.as_view()),
]
