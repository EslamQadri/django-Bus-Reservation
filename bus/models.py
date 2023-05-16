from django.db import models
from django.contrib.auth.models import User

from bus.utils import generate_random_text


# Create your models here.
class Chires(models.Model):
    passanger = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class BusChoies(models.TextChoices):
    VIP = "VIP", "VIP"
    normal = "Noramal", "Noramal"


class Bus(models.Model):
    bus_number = models.CharField(
        max_length=4,
        unique=True,
        blank=False,
        null=False,
        default=generate_random_text(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_chires = models.IntegerField()
    price_of_chir = models.DecimalField(max_digits=4, decimal_places=2)
    type_of_bus = models.CharField(
        max_length=10, choices=BusChoies.choices, default=BusChoies.normal
    )
    chir_number = models.ForeignKey(Chires, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.bus_number}"


class Trip(models.Model):
    frm = models.CharField(
        "from city",
        max_length=40,
    )
    to = models.CharField("to city", max_length=40)
    leave_at = models.DateTimeField()
    arive_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    leave_at = models.DateTimeField()
    arive_at = models.DateTimeField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.bus.bus_number} From {self.frm} To {self.to}"
