from rest_framework import routers

from .views import FlightViewSet

app_name = 'flight'

router = routers.SimpleRouter()
router.register(r'flight', FlightViewSet, basename='flight')
urlpatterns = router.urls