from rest_framework import mixins, viewsets
from rest_framework.response import Response

from rental.models import Rental
from rental.serializers import RentalSerializer


class RentalCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


class RentalUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
