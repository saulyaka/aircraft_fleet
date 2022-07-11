from django.db import models
from django.core.exceptions import ValidationError


def serial_number_validator(value):
    aircrafts = Aircraft.objects.all()
    sn = list(aircraft.serial_number for aircraft in aircrafts)
    if value in sn:
        raise ValidationError(f"Aircraft with {value} serial number already exits.")

    
class Aircraft(models.Model):
    serial_number = models.CharField(max_length=250, validators=[serial_number_validator])
    manufacturer = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.serial_number}, {self.manufacturer}'

    def __repr__(self):
        return f'aircraft {self.serial_number} is added.'
