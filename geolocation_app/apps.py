from django.apps import AppConfig


class GeolocationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geolocation_app'
    verbose_name = 'Geolocation Distance Measurement between 2 locations'
