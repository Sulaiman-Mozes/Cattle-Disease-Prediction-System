from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VeterinaryPlace

# Create your views here.


class MapsListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return VeterinaryPlace.objects.all()


class MapsDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return VeterinaryPlace.objects.all()