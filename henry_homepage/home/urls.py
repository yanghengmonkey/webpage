from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    #url(r'^about$', TemplateView.as_view( template_name = 'home/about.html'), name='about'),
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^contact$', TemplateView.as_view( template_name = 'home/contact.html'), name='contact'),
]

