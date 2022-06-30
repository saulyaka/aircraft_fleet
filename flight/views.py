from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import DjangoObjectPermissions #TODO


from flight.models import Flight
from flight.serializers import FlightSerializer


class FlightViewSet(viewsets.GenericViewSet):
    pass