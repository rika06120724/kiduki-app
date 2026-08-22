from django.urls import path
from .views import create_pet, my_page

app_name = 'pets'
urlpatterns = [
    path('register/', create_pet, name='register'),
    path('my_page/', my_page, name='my_page'),
]
