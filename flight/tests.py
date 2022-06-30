from django.test import TestCase
from datetime import datetime, timedelta
from django.core.exceptions import FieldDoesNotExist

from .models import Flight
# C-R-U-D
class FlightModelTestCase(TestCase):

    def test_airpots(self):
        current_time = datetime.now()
        departure_time = current_time + timedelta(days=1)
        arrival_time = current_time + timedelta(days=2)
        new_flight = Flight.objects.create(
            departure_airport='A1',
            arrival_airport='AN',
            departure_datetime=departure_time,
            arrival_datetime=arrival_time
        )
        new_flight.save()
        self.assertRaisesMessage('sdf', 'asdas')

        new_flight = Flight(
            departure_airport='BG',
            arrival_airport='AN',
            departure_datetime=departure_time,
            arrival_datetime=departure_time
        )
        new_flight.save()
        self.assertRaises(FieldDoesNotExist)



    def test_departure_date(self):
        current_time = datetime.now()
        departure_time = current_time - timedelta(days=1)
        arrival_time = current_time + timedelta(days=1)
        new_flight = Flight(
            departure_airport='BG',
            arrival_airport='AN',
            departure_datetime=departure_time,
            arrival_datetime=arrival_time
        )
        new_flight.save()
        self.assertEquals(new_flight.save(), None)

    def test_arrival_date(self):
        pass


    def test_update_departure_date(self):
        # Since it is not forbidden change date in the past:
        pass

    def test_update_arrival_date(self):
        # Since it is not forbidden change date in the past:
        pass


class FlightViewTestCase(TestCase):
    pass


class FlightSearchTestCase(TestCase):
    pass