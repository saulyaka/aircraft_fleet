from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from aircraft.models import Aircraft
from aircraft.serializers import AircraftSerializer


class AircrafViewSet(viewsets.GenericViewSet):
    """
    A simple GenericViewSet for listing or retrieving aircrafts.
    get:
    Return a list of all the existing aircrafts.
    post:
    Create a new aircraft instance.
    retrieve:
    Return the given aircraft.
    put:
    Update the given aircraft
    delete:
    Delete the given aircraft
    """
    serializer_class = AircraftSerializer
    queryset = Aircraft.objects.all()

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
