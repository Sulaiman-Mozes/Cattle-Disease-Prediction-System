from django.conf.urls import url, include
from .views import  DiseasesEndpoint, DiseaseEndpoint

urlpatterns = [
    url(r'diseases/$', DiseasesEndpoint.as_view(), name='ListCreate'),
    url(r'diseases/(?P<pk>[0-9]+)/$', DiseaseEndpoint.as_view(), name='RetrieveUpdateDestroy'),
]
