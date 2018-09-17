from django.urls import path

from .apps import GeoConfig
from . import views

app_name = GeoConfig.name

urlpatterns = [
    path('', views.geo_home, name='home'),
]
