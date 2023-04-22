from django.urls import path
from .views import Course, Course_detail, course_search, course_name

app_name = 'course'
urlpatterns = [
    path('', Course, name="Course_main"),
    path('<int:pk>/', Course_detail, name='Course_detail'),
    path('search', course_search, name='course_search'),
    path('<str:pk>', course_name, name='course_name')
]
