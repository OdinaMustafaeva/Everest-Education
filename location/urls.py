from django.urls import path
from .views import locations, location_detail, new_add, edit_location, delete_location

app_name = 'location'
urlpatterns = [
    path('', locations, name="location_"),
    path('<int:pk>/', location_detail, name="location_detail"),
    path('add_new', new_add, name="new_add"),
    path('edit/<int:p_k>', edit_location, name="edit"),
    path('delete/<int:pk>', delete_location, name="delete_location")
]
