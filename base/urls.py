from django.urls import path
from .views import Home, register_page, login_page, logout_request, profile_page, chat_page, profile_edit

app_name = 'base'
urlpatterns = [
    path('', Home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path("logout/", logout_request, name="logout"),
    path("profile/", profile_page, name="profile"),
    path("profile/edit", profile_edit, name="profile_edit"),
    path("chat/", chat_page, name="chat")
]
