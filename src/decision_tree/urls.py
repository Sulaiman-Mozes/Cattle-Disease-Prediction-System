from django.views.generic import TemplateView
from django.conf.urls import url, include
from .views import SymptomView, ResultView


urlpatterns = [
    url(r'^$', SymptomView.as_view(), name='diagnose'),
    url(r'^result/$', ResultView.as_view(), name='results'),
]
