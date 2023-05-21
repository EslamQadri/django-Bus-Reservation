from django.contrib import admin
from bus.models import Bus, Chires, Trip

# Register your models here.
admin.site.register((Bus, Chires, Trip))
