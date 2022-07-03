# Title: Aircraft fleet / Repositoriy: saulyaka/aircraft_fleet
# Author: Alla Popova

* Project status: working/dev

# What is it/What does it do:
    The project is developed on Django Framework and containerized in Docker.
    Models: Aircraft and Flight
    For Aircraft CRUD methods avalible by '/api-aircraft/aircraft/'
    For Flight CRUD methods avaliable by '/api-flight/flight/'
    Flight Search/Filtering avaliable by '/api-flight/search/'
    Flight report avaliable by '/api-flight/report/'
    *Notes: Given link for ICAO codes gives the codes of 80-x. They were used.

 
# Instalation
    In the root directory of the priject:
    Creating image:
        In CL: docker-compose build
    When it finish pulling and creating image you can test it (see below) and/or start it with the command:
        In CL: docker-compose up

# Testing
    in CL: docker-compose run --rm web python manage.py test --verbosity 2 --force-color

# UI
    To have for a quick look to functionality Simple UI avaliable by:
        aircrafts CRUD '/api-aircraft/aircraft/'

        flights CRUD '/api-flight/flight/'

        flights search '/api-flight/search/'
            Args: 'departure_datetime_from', 'departure_datetime_ending', 'arrival_airport', 'departure_airport': 'C'
        
        report '/api-flight/report/'
            Args: 'start', 'end':
        *Notes: All date-time args in  datetime python style

    DB is empty. If you want to have a look on UI with some data load fixtures
    in CL: in CL: docker-compose run --rm web python manage.py loaddata aircraft.json
                  docker-compose run --rm web python manage.py loaddata flight.json

# Project tree:
    ├── aircraft
    │   ├── admin.py
    │   ├── apps.py
    │   ├── codes_ICAO.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── aircraft.json
    ├── app
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── docker-compose.yml
    ├── Dockerfile
    ├── flight
    │   ├── admin.py
    │   ├── apps.py
    │   ├── filters.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── flight.json
    ├── manage.py
    ├── README.md
    └── requirements.txt
