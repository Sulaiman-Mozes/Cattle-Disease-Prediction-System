from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class VeterinaryPlace (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    site_image = models.ImageField( height_field="height_field", width_field="width_field")
    height_field = 	models.IntegerField(default=0)
    width_field = 	models.IntegerField(default=0)
    snippet = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("maps:details", kwargs={"pk": self.pk})