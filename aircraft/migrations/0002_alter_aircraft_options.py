# Generated by Django 3.2.13 on 2022-06-29 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraft',
            options={'ordering': ['manufacturer']},
        ),
    ]
