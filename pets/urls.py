from django.urls import path
from .views import create_pet, my_page, pet_edit

app_name = 'pets'
urlpatterns = [
    path('register/', create_pet, name='register'),
    path('my_page/', my_page, name='my_page'),
    path('<int:pet_id>/edit/', pet_edit, name='edit'),  # ペット編集ビューへのURLパターンを追加
]
