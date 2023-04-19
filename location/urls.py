from django.urls import path
from .views import locations

app_name = 'location'
urlpatterns = [
    path('', locations, name="location_")
]
