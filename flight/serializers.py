from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
            'departure_airport',
            'arrival_airport',
            'departure_datetime',
            'arrival_datetime',
            'aircraft',
        )


class FlightReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
            'departure_airport',
            'arrival_airport',
            'departure_datetime',
            'arrival_datetime',
            'aircraft',
        )
