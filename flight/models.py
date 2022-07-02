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

    def clean(self):
        # if aeroport is not in list
        if len(self.departure_airport) > 2 or self.departure_airport not in codes:
            raise ValidationError(
                f'departure airport {self.departure_airport} is not in list',
                params={'departure_airport': self.departure_airport}
            )
        if len(self.arrival_airport) > 2 or self.arrival_airport not in codes:
            raise ValidationError(
                f'arrival airport {self.arrival_airport} is not in list',
                params={'arrival_airport': self.arrival_airport}
            )
        # If the departure date-time is in the past.
        current_time = datetime.now()
        if self.departure_datetime < current_time:
            raise ValidationError(
                f'departure time {self.departure_datetime} has already passed',
                params={'departure_datetime': self.departure_datetime}
            )
        # If arrival date-time comes befor departure date-time.
        if self.arrival_datetime < self.departure_datetime:
            raise ValidationError(
                f'Arrival time {self.arrival_datetime} comes before departure time ',
                params={
                    'arrival_datetime': self.arrival_datetime,
                    'departure_datetime': self.departure_datetime,
                }
            )
