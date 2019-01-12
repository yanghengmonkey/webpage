from django.views import generic
from django.shortcuts import render

class HomeView(generic.base.TemplateView):
    template_name = 'home/index.html'

class AboutView(generic.base.TemplateView):
    template_name = 'home/about.html'
