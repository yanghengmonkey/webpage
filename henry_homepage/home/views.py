from django.views import generic
from django.shortcuts import render

class HomeView(generic.base.TemplateView):
    template_name = 'home/index.html'

