from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

from aircraft.models import Aircraft
from aircraft.codes_ICAO import CODES_ICAO

codes = [CODES_ICAO[i][0] for i in range(0, len(CODES_ICAO))]


def check_airport(value):
    if value not in codes:
        raise ValidationError(
            f'{value} is not in airport list',
            params={'airport': value}
        )


def check_departure_time(value):
    if value < datetime.now():
        raise ValidationError(f'departure time {value} must be in future')


class Flight(models.Model):
    departure_airport = models.CharField(max_length=2, validators=[check_airport])
    arrival_airport = models.CharField(max_length=2, validators=[check_airport])
    departure_datetime = models.DateTimeField(validators=[check_departure_time])
    arrival_datetime = models.DateTimeField()
    aircraft = models.ForeignKey(
        Aircraft,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['departure_datetime']

    def __str__(self):
        return f'departure: {self.departure_airport}-{self.departure_datetime}, arrival: {self.arrival_airport}-{self.arrival_datetime}'

    def __repr__(self):
        return f'flight departure: {self.departure_airport}-{self.departure_datetime}, arrival: {self.arrival_airport}-{self.arrival_datetime} is added.'

    def check_arrival_datetime(self):
        # If arrival date-time comes befor departure date-time.
        if self.arrival_datetime <= self.departure_datetime:
            return False
        else:
            return True
