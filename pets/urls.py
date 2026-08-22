from django.urls import path
from .views import create_pet

app_name = 'pets'
urlpatterns = [
    path('register/', create_pet, name='register'),
]
