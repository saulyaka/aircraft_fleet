from functools import partial
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoObjectPermissions #TODO???????


from flight.models import Flight
from flight.serializers import FlightSerializer


class FlightViewSet(viewsets.GenericViewSet):
    """
    A ViewSet for listing, filtering or retrieving flights.
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['departure_airport', 'arrival_airport']
    search_fields = ['departure_airport', 'arrival_airport']

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    