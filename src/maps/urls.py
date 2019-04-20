from django.conf.urls import url
from .views import MapsDetailView, MapsListView


urlpatterns = [
    url(r'^$', MapsListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', MapsDetailView.as_view(), name='details'),
]
