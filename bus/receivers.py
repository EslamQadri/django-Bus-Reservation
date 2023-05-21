from bus.models import Trip, Chires

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Trip)
def create_cheirs_after_create_trip(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.bus.capacity + 1):
            Chires.objects.create(trip=instance, number_of_chir=i)
