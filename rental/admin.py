from django.contrib import admin

from rental.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        'renter',
        'bike',
        'start_time',
        'end_time',
        'cost',
    )
    search_fields = ('bike',)
    list_filter = ('renter',)
