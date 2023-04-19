from django.urls import path
from .views import Course

app_name = 'course'
urlpatterns = [
    path('', Course, name="Course_main")

]
