from django.urls import path
from .views import Home

app_name = 'base'
urlpatterns = [
    path('', Home, name='home'),
]
