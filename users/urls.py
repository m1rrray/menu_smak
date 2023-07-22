from django.urls import path
from . import views
from .views import UserProfileView, add_address, edit_profile, addresses, delete_address

urlpatterns = [
    path('<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/add_address/', add_address, name='add_address'),
    path('<int:pk>/edit_profile/', edit_profile, name='edit_profile'),
    path('<int:pk>/edit_addresses/', addresses, name='edit_address'),
    path('delete_address/<int:pk>/', delete_address, name='delete_address'),
]