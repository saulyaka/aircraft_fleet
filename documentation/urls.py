from rest_framework.schemas import get_schema_view
from django.urls import path


urlpatterns = [
    path('', get_schema_view(
        title="Aircraft fleet",
        description="API for crafts and flight",
        version="1.0.0"
    ), name='openapi-schema'),
    # ...
]