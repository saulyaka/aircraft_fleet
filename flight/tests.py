from datetime import datetime, timedelta
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.renderers import JSONRenderer
import json
from django.urls import reverse

from .models import Flight
from aircraft.models import Aircraft
from .serializers import FlightSerializer

client = Client()


class CreatNewFlightTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']

    def test_correct_created_flight(self):
        response = client.post(
            '/api-flight/flight/', {
                "departure_airport": "BI",
                "arrival_airport": "C",
                "departure_datetime": "2025-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        flights = Flight.objects.all()
        pk = flights[len(flights) - 1].id
        flight = Flight.objects.get(pk=pk)
        response = client.get(f'/api-flight/flight/{pk}/')
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flight).data))

        response = client.post(
            '/api-flight/flight/', {
                "departure_airport": "BI",
                "arrival_airport": "C",
                "departure_datetime": "2025-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": ""
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        flights = Flight.objects.all()
        pk = flights[len(flights) - 1].id
        flight = Flight.objects.get(pk=pk)
        response = client.get(f'/api-flight/flight/{pk}/')
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flight).data))

    def test_incorrect_airport_(self):
        response = client.post(
            '/api-flight/flight/', {
                "departure_airport": "",
                "arrival_airport": "C",
                "departure_datetime": "2025-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/', {
                "departure_airport": "11",
                "arrival_airport": "C",
                "departure_datetime": "2025-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/', {
                "departure_airport": "BI",
                "arrival_airport": "",
                "departure_datetime": "2025-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.post(
            '/api-flight/flight/', {
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
            '/api-flight/flight/', {
                "departure_airport": "BG",
                "arrival_airport": "C",
                "departure_datetime": "2020-10-04T18:30:00",
                "arrival_datetime": "2025-10-04T22:30:00",
                "aircraft": 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FlightListTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']

    def test_list_flight(self):
        response = client.get('/api-flight/flight/')
        flights = Flight.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flights, many=True).data))


class FlightDeleteTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']

    def test_delete_flight(self):
        response = client.get(f'/api-flight/flight/{6}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.delete(f'/api-flight/flight/{6}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FlightPutTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']
    valid_payload = {
        "departure_airport": "BI",
        "arrival_airport": "C",
        "departure_datetime": "2025-10-04T18:30:00",
        "arrival_datetime": "2025-10-04T22:30:00",
        "aircraft": ""
    }
    invalid_payload_airport = {
        "departure_airport": "BI",
        "arrival_airport": "Canada",
        "departure_datetime": "2025-10-04T18:30:00",
        "arrival_datetime": "2025-10-04T22:30:00",
        "aircraft": ""
    }
    invalid_payload_datetime = {
        "departure_airport": "BI",
        "arrival_airport": "Canada",
        "departure_datetime": "Some wrong time format",
        "arrival_datetime": "2025-10-04T22:30:00",
        "aircraft": ""
    }

    def test_valid_update_flight(self):
        response = client.put(
            f'/api-flight/flight/{4}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_invalid_update_airport(self):
        response = client.put(
            f'/api-flight/flight/{4}/',
            data=json.dumps(self.invalid_payload_airport),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_update_datetime(self):
        response = client.put(
            f'/api-flight/flight/{4}/',
            data=json.dumps(self.invalid_payload_datetime),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FlightSearchTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']

    def test_departure_airport_search(self):
        airport = 'BG'
        response = client.get(f'/api-flight/search/?departure_airport={airport}')
        flights = Flight.objects.filter(departure_airport=airport)
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flights, many=True).data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_arrival_airport_search(self):
        airport = 'C'
        response = client.get(f'/api-flight/search/?arrival_airport={airport}')
        flights = Flight.objects.filter(arrival_airport=airport)
        self.assertEqual(response.content, JSONRenderer().render(FlightSerializer(flights, many=True).data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_departure_and_arrival_airport_search(self):
        pass

    def test_departure_datetime_search(self):
        pass

    def test_departure_and_arrival_datetime_search(self):
        pass

    def test_departure_and_arrival_datetime__departure_and_arrival_airport_search(self):
        pass

    def test_incorrect_search(self):
        pass


class FlightReportTest(TestCase):
    fixtures = ['aircraft.json', 'flight.json']
