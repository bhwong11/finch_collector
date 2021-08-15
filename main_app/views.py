from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from .models import Finch
from django.urls import reverse

from django.http import HttpResponse

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'
    # def get(self,request):
    #     return HttpResponse('Hit Home')


class About(TemplateView):
    template_name = 'about.html'


class FinchList(TemplateView):
    template_name = 'finch_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['finches'] = Finch.objects.filter(name__icontains=name)
        else:
            context['finches'] = Finch.objects.all()
        return context


class FinchCreate(CreateView):
    model = Finch
    template_name = 'finch_create.html'
    fields = ['name', 'img', 'cool', 'color']

    def get_success_url(self):
        return reverse('finch_details', kwargs={'pk': self.object.pk})


class FinchDetail(DetailView):
    model = Finch
    template_name = 'finch_details.html'


class FinchUpdate(UpdateView):
    model = Finch
    template_name = 'finch_update.html'
    fields = ['name', 'img', 'cool', 'color']

    def get_success_url(self):
        return reverse('finch_details', kwargs={'pk': self.object.pk})
