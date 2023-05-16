from django.db import models
from django.contrib.auth.models import User
from bus.models import Trip


# Create your models here.
class Ticket(models.Model):
    passanger = models.ForeignKey(User, on_delete=models.RESTRICT)
    trip = models.ForeignKey(Trip, on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        self.date_of_travel = self.trip.leave_at
        super().save(*args, **kwargs)
