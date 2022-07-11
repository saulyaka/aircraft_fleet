from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters

from flight.models import Flight
from flight.serializers import FlightSerializer, FlightReportSerializer
from flight.filters import FlightFilter, FlightReportFilter


class FlightViewSet(viewsets.GenericViewSet):
    """
    A ViewSet for listing, filtering or retrieving flights.
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()

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
        flight = Flight.objects.create(
            departure_airport=request.data['departure_airport'],
            arrival_airport=request.data['arrival_airport'],
            departure_datetime=request.data['departure_datetime'],
            arrival_datetime=request.data['arrival_datetime'],
            aircraft=None
        )
        if flight.check_arrival_datetime():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

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


class FlightListFiltered(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightFilter


class FlightReport(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightReportSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightReportFilter
