from rest_framework import status
from django.test import TestCase, Client
from rest_framework.renderers import JSONRenderer
import json

from .models import Aircraft
from .serializers import AircraftSerializer

client = Client()


class AircraftTest(TestCase):
    """ Test model Aircraft and"""
    fixtures = ['aircraft.json']

    def setUp(self):
        self.aircraft = Aircraft.objects.create(
            serial_number='10-01LKKJHGFF0000', manufacturer='Boeing')

    def test_creation_aircraft(self):
        # Correct data
        response = client.post(
            '/api-aircraft/aircraft/',
            {'serial_number': '124asdAS!@#$%^&*()', 'manufacturer': '0908673_____!@#$%^asdfMNB'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        aircraft = Aircraft.objects.get(serial_number='124asdAS!@#$%^&*()')
        response = client.get(f'/api-aircraft/aircraft/{aircraft.id}/')
        self.assertEqual(response.content, JSONRenderer().render(AircraftSerializer(aircraft).data))

        # Incorrect data
        response = client.post(
            '/api-aircraft/aircraft/',
            {'serial_number': '', 'manufacturer': '0908673_____!@#$%^asdfMNB'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # With existing serial number
        response = client.post(
            '/api-aircraft/aircraft/',
            {'serial_number': '10-01LKKJHGFF0000', 'manufacturer': 'Boeing'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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


class UpdateSingleAircraftTest(TestCase):
    """ Test module for updating an existing aircraft record """

    def setUp(self):
        self.aircraft = Aircraft.objects.create(
            serial_number='10-01LKKJHGFF0000', manufacturer='Some S.L')

        self.valid_payload = {
            'serial_number': '99887766',
            'manufacturer': 'Boeing',
        }
        self.invalid_payload = {
            'serial_number': '10-01LKKJHGFF0000',
            'manufacturer': '',
        }

    def test_valid_update_aircraft(self):
        response = client.put(
            f'/api-aircraft/aircraft/{self.aircraft.id}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_invalid_update_aircraft(self):
        response = client.put(
            f'/api-aircraft/aircraft/{self.aircraft.id}/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
