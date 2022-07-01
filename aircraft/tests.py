from rest_framework import status
from django.test import TestCase, Client
from rest_framework.renderers import JSONRenderer

from .models import Aircraft
from .serializers import AircraftSerializer

client = Client()

class AircraftTest(TestCase):
    """ Test model Aircraft and CRUD"""
    fixtures = ['aircraft.json'] 

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
        pass
    """
        # Correct data
        response = client.patch('/api-aircraft/aircraft/1/', data={'manufacturer': 'Some S.L.'})
        aircraft = Aircraft.objects.get(pk=1)
        self.assertEqual(response.content, JSONRenderer().render(AircraftSerializer(aircraft).data))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Incorrect data
    """
