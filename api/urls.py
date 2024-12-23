from django.urls import path
from . import views
urlpatterns = [
    path('addusers/',views.AdminAddUsersApi.as_view()),
    path('additional/',views.RegistrationUserApi.as_view()),
]