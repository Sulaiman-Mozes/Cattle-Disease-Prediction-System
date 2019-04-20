from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Disease


class DiseaseListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Disease.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(DiseaseListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		item_exists = Disease.objects.all().exists()
		qs = Disease.objects.all().search(query)
		if item_exists and qs.exists():
			context['search'] = qs
		return context


class TipListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Tip.objects.all()


class DiseaseDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Disease.objects.all()


class TipDetailView(LoginRequiredMixin, DetailView):	
	def get_queryset(self):
		return Tip.objects.all()
