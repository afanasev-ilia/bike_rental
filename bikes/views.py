from rest_framework import mixins, viewsets

from bikes.models import Bike
from bikes.serializers import BikeSerializer


class BikeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet,):
    queryset = Bike.objects.filter(is_rented=False)
    serializer_class = BikeSerializer
