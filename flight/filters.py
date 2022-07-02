from cProfile import label
from django_filters import rest_framework as filters
from .models import Flight


class FlightFilter(filters.FilterSet):
    departure_airport = filters.CharFilter(field_name='departure_airport')
    arrival_airport = filters.CharFilter(field_name='arrival_airport')
    departure_datetime_from = filters.DateTimeFilter(field_name='departure_datetime', lookup_expr='gte')
    departure_datetime_ending = filters.DateTimeFilter(field_name='departure_datetime', lookup_expr='lte')

    class Meta:
        model = Flight
        fields = ['departure_airport', 'arrival_airport', 'departure_datetime_from', 'departure_datetime_ending']


class FlightReportFilter(filters.FilterSet):
    start = filters.DateTimeFilter(field_name='arrival_datetime', lookup_expr='gte', label="Initial date and time of period")
    end = filters.DateTimeFilter(field_name='departure_datetime', lookup_expr='lte', label="Final date and time of period")

    class Meta:
        model = Flight
        fields = ['departure_datetime', 'arrival_datetime']
