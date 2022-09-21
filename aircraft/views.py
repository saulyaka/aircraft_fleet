from rest_framework import status, viewsets
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from aircraft.models import Aircraft
from aircraft.serializers import AircraftSerializer


class AircrafViewSet(viewsets.GenericViewSet):
    """
    A simple GenericViewSet for aircrafts CRUD operations
    """
    serializer_class = AircraftSerializer
    queryset = Aircraft.objects.all()

    def list(self, request):
        """
        Return a list of all existing aircrafts
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        Return the given aircraft
        """
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create a new aircraft instance
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update the given aircraft
        """
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        """
        Delete the given aircraft
        """
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
