from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chires(models.Model):
    passanger = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class BusChoies(models.TextChoices):
    VIP = "VIP", "VIP"
    normal = "Noramal", "Noramal"


class Bus(models.Model):
    bus_number = models.CharField(max_length=25, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="trip_created"
    )
    number_of_chires = models.IntegerField()
    price_of_chir = models.DecimalField(max_digits=4, decimal_places=2)
    leave_at = models.DateTimeField()
    arive_at = models.DateTimeField()
    frm = models.CharField(
        "from city",
        max_length=40,
    )
    to = models.CharField("to city", max_length=40)
    type_of_bus = models.CharField(max_length=20)
    chir_number = models.ForeignKey(Chires, on_delete=models.CASCADE)
    
