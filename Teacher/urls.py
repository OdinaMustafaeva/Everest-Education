from django.urls import path
from .views import Teacher, Teacher_detail

app_name = 'teacher'
urlpatterns = [
    path('', Teacher, name="teacher_"),
    path('<int:pk>/', Teacher_detail, name="teacher_detail")
]
