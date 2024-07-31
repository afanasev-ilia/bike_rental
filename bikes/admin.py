from django.contrib import admin

from bikes.models import Bike


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = (
        'bike_model',
        'serial_number',
        'is_rented',
        'rental_price',
    )
    search_fields = ('serial_number',)
    list_filter = ('serial_number',)
