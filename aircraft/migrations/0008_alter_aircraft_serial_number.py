# Generated by Django 3.2.13 on 2022-07-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0007_alter_aircraft_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='serial_number',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]