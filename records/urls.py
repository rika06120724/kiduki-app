
from django.urls import path

from .views import create_record



app_name = "records"

urlpatterns = [

    path("<int:pet_id>/create/", create_record, name="create"),

]

