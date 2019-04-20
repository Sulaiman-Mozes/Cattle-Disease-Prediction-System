from django.db import models
#from django.core.urlresolvers import reverse
#from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from rest_framework.reverse import reverse

# Create your models here.


class DiseaseQuerySet(models.query.QuerySet):
	def search(self, query):
		if query:
			query = query.strip()
			return self.filter(
				Q(disease__icontains=query)|
				Q(description__icontains=query)|
				Q(causes__icontains=query)|
				Q(treatment__icontains=query)|
				Q(prevention__icontains=query)
				).distinct()
		return self


class DiseaseManager(models.Manager):

	def get_queryset(self):
		return DiseaseQuerySet(self.model, using=self._db)

	def search(self, query):
		return self.get_queryset().search(query)


class Tip(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(blank=True, null=True, height_field = "height_field", width_field = "width_field")
	height_field = 	models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ("info:tip-detail", kwargs={"pk":self.pk})


class Disease(models.Model):
	disease = models.CharField(max_length = 50)
	description = models.TextField()
	causes = models.TextField()
	symptoms = models.TextField()
	treatment = models.TextField()
	prevention = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = DiseaseManager()

	def __str__ (self):
		return self.disease

	def get_absolute_url(self):
		return reverse("info:disease-detail", kwargs={"pk":self.pk})

	def get_api_url(self, request=None):
		return reverse("api:RetrieveUpdateDestroy", kwargs={"pk":self.pk}, request=request)
