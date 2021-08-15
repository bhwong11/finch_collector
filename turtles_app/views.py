from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from django.http import HttpResponse

# Create your views here.


class Turtle:
    def __init__(self, species, cool):
        self.species = species
        self.cool = cool


turtles = [
    Turtle('t1', True),
    Turtle('t2', True),
    Turtle('t2', True),
]


class Home(TemplateView):
    template_name = 'turtle_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['turtless'] = turtles
        return context
