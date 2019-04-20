from django.views.generic import TemplateView
from django.conf.urls import url
from .views import ContactView


urlpatterns = [
   url(r'^$', ContactView.as_view(), name='contact')

]