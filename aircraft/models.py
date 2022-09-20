from django.db import models
from django.core.exceptions import ValidationError


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=250, unique=True)
    manufacturer = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.serial_number}, {self.manufacturer}'

    def __repr__(self):
        return f'aircraft {self.serial_number}'
