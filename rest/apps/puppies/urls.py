from django.urls import path

from .apps import PuppiesConfig
from . import views

app_name = PuppiesConfig.name

urlpatterns = [
    path(
        'api/v1/puppies/<int:pk>',
        view=views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    path(
        'api/v1/puppies/',
        view=views.get_post_puppies,
        name='get_post_puppies'
    ),
]
