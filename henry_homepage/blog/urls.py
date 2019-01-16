from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDeleteView.as_view(), name='delete'),
    url(r'^tag/(?P<tag>\w+)/$', views.tagpage, name='tagpage'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search_hs/', include('haystack.urls')),
]

