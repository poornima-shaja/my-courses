from django.contrib import admin
from .models import *
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display=("id", "origin","destination", "duration")

class AirportAdmin(admin.ModelAdmin):
    list_display=("id", "city","code")

class PassengerAdmin(admin.ModelAdmin):
    list_display=("id", "first","last", "flight")

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passengers)
