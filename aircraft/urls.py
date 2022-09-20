from rest_framework import routers

from .views import AircrafViewSet

app_name = 'aircraft'

router = routers.SimpleRouter()
router.register(r'', AircrafViewSet, basename='aircraft')
urlpatterns = router.urls
