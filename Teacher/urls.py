from django.urls import path
from .views import Teacher

app_name = 'teacher'
urlpatterns = [
    path('', Teacher, name="teacher_")
]
