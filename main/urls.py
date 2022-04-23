# Django Imports
from django.urls import path, include

# Standard Package Imports

# Project Imports
from . import views


# Third Party Imports


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]