from django.urls import path
from .views import Course, Course_detail, course_search, new_add, course_edit, course_delete

app_name = 'course'
urlpatterns = [
    path('', Course, name="Course_main"),
    path('<str:pk>/', Course_detail, name='Course_detail'),
    path('search/', course_search, name='course_search'),
    path('new_add', new_add, name='new_add'),
    path('edit/<str:p_k>', course_edit, name='course_edit'),
    path('delete/<str:pk>', course_delete, name='course_delete'),
]
