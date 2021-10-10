from django.urls import path
from . import views

app_name = 'geolocation_app'

urlpatterns = [
    path('',views.calculate_distance_view, name='calculate_distance'),
]