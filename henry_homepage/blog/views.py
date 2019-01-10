from django.views import generic
from django.shortcuts import render

class IndexView(generic.base.TemplateView):
    template_name = 'blog/index.html'

