from django.urls import path
from .views import textbook

app_name = 'textbook'
urlpatterns = [
    path('', textbook, name="textbook_")
]
