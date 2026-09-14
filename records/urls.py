from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('create/<int:pet_id>/', views.create_record, name='create'),
]