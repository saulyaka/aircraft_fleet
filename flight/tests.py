from datetime import datetime, timedelta
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.renderers import JSONRenderer

from .models import Flight
from aircraft.models import Aircraft
from .serializers import FlightSerializer

client = Client()

class FlightTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json'] 

    def test_correct_created_flight(self):
        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "BI",
            "arrival_airport": "C",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        flights = Flight.objects.all()
        pk = flights[len(flights) -1].id
        flight = Flight.objects.get(pk=pk)
        response = client.get(f'/api-flight/flight/{pk}/')
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flight).data))

        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "BI",
            "arrival_airport": "C",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": ""
            }
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        flights = Flight.objects.all()
        pk = flights[len(flights) -1].id
        flight = Flight.objects.get(pk=pk)
        response = client.get(f'/api-flight/flight/{pk}/')
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flight).data))

    def test_incorrect_airport_(self):
        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "",
            "arrival_airport": "C",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "11",
            "arrival_airport": "C",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "BI",
            "arrival_airport": "",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "",
            "arrival_airport": "C",
            "departure_datetime": "2025-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_incorrect_departure_time(self):
        response = client.post(
            '/api-flight/flight/',
            {
            "departure_airport": "BG",
            "arrival_airport": "C",
            "departure_datetime": "2020-10-04T18:30:00",
            "arrival_datetime": "2025-10-04T22:30:00",
            "aircraft": 1
            }
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class FlightFilterTest(TestCase):
    pass
"""
    def test_delete_aircraft(self):
        response = client.post(
            '/api-aircraft/aircraft/',
            {'serial_number': '124asdAS!@#$%^&*()', 'manufacturer': '0908673_____!@#$%^asdfMNB'}
            )
        aircraft = Aircraft.objects.get(serial_number='124asdAS!@#$%^&*()')
        response = client.delete(f'/api-aircraft/aircraft/{aircraft.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
    def test_list_aircraft(self):
        response = client.get('/api-aircraft/aircraft/')
        aircrafts = Aircraft.objects.all()
        self.assertEqual(response.content, JSONRenderer().render(AircraftSerializer(aircrafts, many=True).data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_update_aircraft(self):
        # Correct data
        response = client.patch('/api-aircraft/aircraft/1/', data={'manufacturer': 'Some S.L.'})
        aircraft = Aircraft.objects.get(pk=1)
        self.assertEqual(response.content, JSONRenderer().render(AircraftSerializer(aircraft).data))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Incorrect data



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
"""