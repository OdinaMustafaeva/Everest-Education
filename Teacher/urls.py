from django.urls import path
from .views import Teacher, Teacher_detail, new_add, teacher_edit, teacher_delete

app_name = 'teacher'
urlpatterns = [
    path('', Teacher, name="teacher_"),
    path('<int:pk>/', Teacher_detail, name="teacher_detail"),
    path('new_add', new_add, name='new_add'),
    path('edit/<str:p_k>', teacher_edit, name='teacher_edit'),
    path('delete/<str:pk>', teacher_delete, name='teacher_delete'),
]
