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
    datetime = filters.DateTimeFilter(method='custom_filter')

    class Meta:
        model = Flight
        fields = ['departure_datetime', 'arrival_datetime']

    def custom_filter(self, queryset, start_time, end_time):
        report = []
        for flight in queryset:
            if (
                flight.arrival_datetime <= start_time and flight.departure_datetime >= start_time
            ) or (
                flight.arrival_datetime <= end_time and flight.departure_datetime >= end_time
            ) or (
                flight.arrival_datetime >= start_time and flight.deparure_datetime <= end_time
            ) or (
                flight.arrival_datetime <= start_time and flight.departure_datetime >= end_time
            ):
                report.append(flight)
        return report
