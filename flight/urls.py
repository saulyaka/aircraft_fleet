from rest_framework import routers
from django.urls import path

from .views import FlightViewSet, FlightListFiltered, FlightReport
from .models import Flight

app_name = 'flight'

router = routers.SimpleRouter()
router.register(r'', FlightViewSet, basename='flight')

urlpatterns = [
    path(r'search/', FlightListFiltered.as_view(model=Flight), name='search'),
    path(r'report/', FlightReport.as_view(), name='report'),
]
urlpatterns +=  router.urls