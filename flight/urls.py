from rest_framework import routers
from django.urls import path

from .views import FlightViewSet, FlightListFiltered, FlightReport

app_name = 'flight'

router = routers.SimpleRouter()
router.register(r'', FlightViewSet, basename='flight')

urlpatterns = router.urls
urlpatterns.append(path(r'search/', FlightListFiltered.as_view(), name='search'))
urlpatterns.append(path(r'report/', FlightReport.as_view(), name='report'))
