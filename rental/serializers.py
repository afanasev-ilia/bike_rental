from rest_framework import serializers

from rental.models import Rental


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = (
            'renter',
            'bike',
            'start_time',
            'end_time',
            'cost',
        )
        read_only_fields = (
            'renter',
            'start_time',
            'end_time',
            'cost',
        )
