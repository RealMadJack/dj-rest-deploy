from django.urls import path

from .apps import PuppiesConfig
from . import views

app_name = PuppiesConfig.name

urlpatterns = [
    path(
        'puppies/<int:pk>',
        view=views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    path(
        'puppies/',
        view=views.get_post_puppies,
        name='get_post_puppies'
    ),
]
