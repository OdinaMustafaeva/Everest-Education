from django.urls import path
from .views import locations, location_detail

app_name = 'location'
urlpatterns = [
    path('', locations, name="location_"),
    path('<int:pk>/', location_detail, name="location_detail")
]
