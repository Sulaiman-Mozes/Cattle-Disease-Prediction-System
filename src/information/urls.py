from django.conf.urls import url, include
from .views import DiseaseDetailView, DiseaseListView, TipDetailView, TipListView

urlpatterns = [
    url(r'^disease/$', DiseaseListView.as_view(), name='list'),
    url(r'^disease/(?P<pk>[0-9]+)/$', DiseaseDetailView.as_view(), name='disease-detail'),
    url(r'^health-tips/(?P<pk>[0-9]+)/$', TipDetailView.as_view(), name='tip-detail'),
    url(r'^health-tips/$', TipListView.as_view(), name='list-health'),
]
