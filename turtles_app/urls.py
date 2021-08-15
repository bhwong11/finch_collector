from turtles_app import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
