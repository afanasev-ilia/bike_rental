from rest_framework import serializers

from bikes.models import Bike


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = (
            'bike_model',
            'serial_number',
            'rental_price',
        )
