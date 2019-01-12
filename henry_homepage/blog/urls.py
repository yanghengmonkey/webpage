from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tag>\w+)/$', views.tagpage, name='tagpage'),
    url(r'^search/$', views.search, name='search'),
]

