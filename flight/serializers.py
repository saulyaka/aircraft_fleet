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


class FlightReportSerializer(serializers.Serializer):

    @staticmethod
    def datetime_converter(interval):
        """
            Convert datetime instance to minutes.
        """
        seconsds = interval.seconds
        minutes = int(seconsds / 60)
        return minutes

    def to_representation(self, instance):
        """
        Method is hardwired to model fields.
        """
        flights = self.instance
        airports_list = set()
        # Get the list of airports
        if flights:
            for flight in flights:
                airports_list.add(flight.departure_airport)
            data = dict()
            for airport in airports_list:
                airport_report = dict()
                airport_report['number_of_departures'] = 0
                airport_report['flights'] = []
                for flight in flights:
                    if flight.departure_airport == airport:
                        airport_report['number_of_departures'] += 1
                        flight.in_flight = flight.arrival_datetime - flight.departure_datetime
                        airport_report['flights'].append(
                            {
                                'id': flight.id,
                                'flight_time': self.datetime_converter(flight.in_flight)
                            }
                        )
                data[airport] = airport_report
            self.instance = None
            return data
        else:
            return None
